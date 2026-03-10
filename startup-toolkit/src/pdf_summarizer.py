"""PDF Reading and Summarization Module using Abacus.AI SDK

This module provides functionality to read PDF files and generate summaries
using the Abacus.AI platform's document processing and LLM capabilities.
"""

import abacusai
import json
from typing import Optional, List, Dict, Any
import os
from pathlib import Path


class PDFSummarizer:
    """A class to handle PDF reading and summarization using Abacus.AI SDK.
    
    This class provides methods to:
    - Extract text from PDF documents
    - Generate summaries using LLMs
    - Extract specific information from PDFs
    
    Attributes:
        client: An authenticated Abacus.AI API client
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the PDFSummarizer with an Abacus.AI client.
        
        Args:
            api_key: Optional API key. If not provided, will use ABACUS_API_KEY
                    environment variable.
        """
        if api_key:
            self.client = abacusai.ApiClient(api_key=api_key)
        else:
            # Uses ABACUS_API_KEY environment variable by default
            self.client = abacusai.ApiClient()
    
    def read_pdf_file(self, pdf_path: str) -> bytes:
        """Read a PDF file and return its bytes.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            PDF file content as bytes
            
        Raises:
            FileNotFoundError: If the PDF file doesn't exist
        """
        pdf_file = Path(pdf_path)
        if not pdf_file.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        with open(pdf_file, 'rb') as f:
            return f.read()
    
    def extract_text_from_pdf(self, 
                              pdf_path: Optional[str] = None,
                              pdf_bytes: Optional[bytes] = None,
                              start_page: Optional[int] = None,
                              end_page: Optional[int] = None) -> str:
        """Extract text content from a PDF document.
        
        Args:
            pdf_path: Path to the PDF file (provide either pdf_path or pdf_bytes)
            pdf_bytes: PDF content as bytes (provide either pdf_path or pdf_bytes)
            start_page: Optional starting page number (0-indexed)
            end_page: Optional ending page number (0-indexed)
            
        Returns:
            Extracted text from the PDF
            
        Raises:
            ValueError: If neither pdf_path nor pdf_bytes is provided
        """
        if pdf_path:
            pdf_bytes = self.read_pdf_file(pdf_path)
        elif pdf_bytes is None:
            raise ValueError("Either pdf_path or pdf_bytes must be provided")
        
        # Extract document data using Abacus.AI
        result = self.client.extract_document_data(
            document=pdf_bytes,
            start_page=start_page,
            end_page=end_page,
            return_extracted_page_text=True
        )
        
        # Combine text from all pages
        if hasattr(result, 'pages') and result.pages:
            text_parts = []
            for page in result.pages:
                if hasattr(page, 'text') and page.text:
                    text_parts.append(page.text)
            return "\n\n".join(text_parts)
        
        return ""
    
    def summarize_text(self,
                      text: str,
                      max_length: int = 500,
                      style: str = "concise",
                      llm_name: Optional[str] = None) -> str:
        """Generate a summary of the provided text using Abacus.AI LLM.
        
        Args:
            text: The text to summarize
            max_length: Maximum length of the summary in tokens
            style: Summary style - 'concise', 'detailed', or 'bullet_points'
            llm_name: Optional specific LLM model to use
            
        Returns:
            Generated summary text
        """
        # Create appropriate prompt based on style
        style_prompts = {
            "concise": "Provide a concise summary of the following text in 2-3 sentences:",
            "detailed": "Provide a detailed summary of the following text, covering all main points:",
            "bullet_points": "Summarize the following text as a list of key bullet points:"
        }
        
        prompt = style_prompts.get(style, style_prompts["concise"])
        full_prompt = f"{prompt}\n\n{text}"
        
        # Use evaluate_prompt for direct LLM access
        response = self.client.evaluate_prompt(
            prompt=full_prompt,
            llm_name=llm_name,
            max_tokens=max_length,
            temperature=0.3
        )
        
        if hasattr(response, 'content'):
            return response.content
        return str(response)
    
    def summarize_pdf(self,
                     pdf_path: Optional[str] = None,
                     pdf_bytes: Optional[bytes] = None,
                     max_length: int = 500,
                     style: str = "concise",
                     start_page: Optional[int] = None,
                     end_page: Optional[int] = None,
                     llm_name: Optional[str] = None) -> Dict[str, Any]:
        """Extract text from a PDF and generate a summary.

        This is a convenience method that combines text extraction and summarization.

        Args:
            pdf_path: Path to the PDF file
            pdf_bytes: PDF content as bytes
            max_length: Maximum length of the summary in tokens
            style: Summary style - 'concise', 'detailed', or 'bullet_points'
            start_page: Optional starting page number
            end_page: Optional ending page number
            llm_name: Optional specific LLM model to use

        Returns:
            Dictionary containing:
                - 'text': Extracted text from PDF
                - 'summary': Generated summary
                - 'page_count': Number of pages processed
                - 'text_length': Length of extracted text
                - 'json_output': JSON string with document name and one-line summary
        """
        # Extract text from PDF
        extracted_text = self.extract_text_from_pdf(
            pdf_path=pdf_path,
            pdf_bytes=pdf_bytes,
            start_page=start_page,
            end_page=end_page
        )

        # Generate summary
        summary = self.summarize_text(
            text=extracted_text,
            max_length=max_length,
            style=style,
            llm_name=llm_name
        )

        # Generate one-line summary
        one_line_response = self.client.evaluate_prompt(
            prompt=f"Summarize the following text in exactly one sentence:\n\n{extracted_text}",
            llm_name=llm_name,
            max_tokens=100,
            temperature=0.3
        )
        one_line_summary = one_line_response.content if hasattr(one_line_response, 'content') else str(one_line_response)

        # Extract document name
        document_name = Path(pdf_path).name if pdf_path else "document.pdf"

        # Count pages (approximate based on text length)
        page_count = len(extracted_text.split('\n\n'))

        # Create JSON output with document name and one-line summary
        json_output = json.dumps({
            "document_name": document_name,
            "one_line_summary": one_line_summary
        }, indent=2)

        return {
            'text': extracted_text,
            'summary': summary,
            'page_count': page_count,
            'text_length': len(extracted_text),
            'json_output': json_output
        }
    
    def extract_key_information(self,
                               pdf_path: Optional[str] = None,
                               pdf_bytes: Optional[bytes] = None,
                               query: str = "What are the main topics?",
                               llm_name: Optional[str] = None) -> str:
        """Extract specific information from a PDF based on a query.
        
        Args:
            pdf_path: Path to the PDF file
            pdf_bytes: PDF content as bytes
            query: The question or information to extract
            llm_name: Optional specific LLM model to use
            
        Returns:
            Answer to the query based on PDF content
        """
        # Extract text from PDF
        extracted_text = self.extract_text_from_pdf(
            pdf_path=pdf_path,
            pdf_bytes=pdf_bytes
        )
        
        # Create prompt for information extraction
        prompt = f"""Based on the following document, answer this question: {query}

Document content:
{extracted_text}

Answer:"""
        
        # Get response from LLM
        response = self.client.evaluate_prompt(
            prompt=prompt,
            llm_name=llm_name,
            max_tokens=500,
            temperature=0.2
        )
        
        if hasattr(response, 'content'):
            return response.content
        return str(response)


def quick_summarize(pdf_path: str, style: str = "concise") -> str:
    """Quick function to summarize a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        style: Summary style - 'concise', 'detailed', or 'bullet_points'
        
    Returns:
        Summary of the PDF
    """
    summarizer = PDFSummarizer()
    result = summarizer.summarize_pdf(pdf_path=pdf_path, style=style)
    return result['summary']


if __name__ == "__main__":
    # Example usage
    print("PDF Summarizer Module")
    print("=====================")
    print("\nThis module provides PDF reading and summarization capabilities.")
    print("\nExample usage:")
    print("""    
    from pdf_summarizer import PDFSummarizer
    
    # Initialize the summarizer
    summarizer = PDFSummarizer()
    
    # Summarize a PDF
    result = summarizer.summarize_pdf('document.pdf', style='concise')
    print(result['summary'])
    """)
