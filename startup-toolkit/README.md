# AbacusStartup

A comprehensive toolkit for working with the Abacus.AI platform, featuring PDF reading and summarization capabilities powered by advanced AI models.

## 🚀 Features

### PDF Reading and Summarization
- **Text Extraction**: Extract text content from PDF documents with page-specific control
- **AI-Powered Summarization**: Generate summaries in multiple styles (concise, detailed, bullet points)
- **Question Answering**: Extract specific information from PDFs using natural language queries
- **Batch Processing**: Process multiple PDF files efficiently
- **Flexible Input**: Work with file paths or PDF bytes directly

### Abacus.AI Integration
- Easy access to Abacus.AI projects and resources
- Pre-configured SDK integration
- Document processing and LLM capabilities

## 📋 Prerequisites

Before using this toolkit, you'll need:

1. **Python 3.8 or higher**
2. **Abacus.AI Account**: Sign up at [Abacus.AI](https://abacus.ai)
3. **API Key**: Get your API key from the Abacus.AI dashboard

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/straulino/AbacusStartup.git
cd AbacusStartup
```

### 2. Install Dependencies

```bash
pip install abacusai
```

For development and running notebooks:

```bash
pip install abacusai jupyter notebook
```

### 3. Set Up API Key

Set your Abacus.AI API key as an environment variable:

**Linux/Mac:**
```bash
export ABACUS_API_KEY='your_api_key_here'
```

**Windows (Command Prompt):**
```cmd
set ABACUS_API_KEY=your_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:ABACUS_API_KEY='your_api_key_here'
```

For permanent setup, add the export command to your shell configuration file (`.bashrc`, `.zshrc`, etc.).

## 📖 Usage

### Quick Start: PDF Summarization

```python
from src.pdf_summarizer import quick_summarize

# Summarize a PDF in one line
summary = quick_summarize('document.pdf', style='concise')
print(summary)
```

### Using the PDFSummarizer Class

```python
from src.pdf_summarizer import PDFSummarizer

# Initialize the summarizer
summarizer = PDFSummarizer()

# Extract text from a PDF
text = summarizer.extract_text_from_pdf(pdf_path='document.pdf')

# Generate a summary
result = summarizer.summarize_pdf(
    pdf_path='document.pdf',
    style='detailed',  # Options: 'concise', 'detailed', 'bullet_points'
    max_length=800
)

print(f"Summary: {result['summary']}")
print(f"Pages processed: {result['page_count']}")
print(f"Text length: {result['text_length']} characters")
```

### Extract Specific Information

```python
# Ask questions about the PDF content
answer = summarizer.extract_key_information(
    pdf_path='document.pdf',
    query='What are the main conclusions?'
)
print(answer)
```

### Process Specific Pages

```python
# Extract text from pages 0-5
text = summarizer.extract_text_from_pdf(
    pdf_path='document.pdf',
    start_page=0,
    end_page=5
)
```

### Working with PDF Bytes

```python
# Read PDF as bytes
with open('document.pdf', 'rb') as f:
    pdf_bytes = f.read()

# Summarize using bytes
result = summarizer.summarize_pdf(pdf_bytes=pdf_bytes, style='concise')
```

## 📓 Interactive Demo

Explore the full capabilities with our Jupyter notebook:

```bash
jupyter notebook notebooks/pdf_demo.ipynb
```

The notebook includes:
- Step-by-step examples
- Different summary styles
- Question answering demonstrations
- Batch processing examples
- Best practices and tips

## 📁 Project Structure

```
AbacusStartup/
├── src/
│   └── pdf_summarizer.py      # PDF processing and summarization module
├── notebooks/
│   └── pdf_demo.ipynb          # Interactive demonstration notebook
├── abacus_sdk_easy.ipynb       # Abacus.AI SDK introduction
├── README.md                    # This file
└── .gitignore                   # Git ignore rules
```

## 🎯 Summary Styles

The PDF summarizer supports three different summary styles:

1. **Concise** (`style='concise'`)
   - Quick overview in 2-3 sentences
   - Best for: Quick understanding of document content

2. **Detailed** (`style='detailed'`)
   - Comprehensive summary covering all main points
   - Best for: In-depth understanding while saving time

3. **Bullet Points** (`style='bullet_points'`)
   - Key points in list format
   - Best for: Easy scanning and reference

## 🔑 API Key Management

**Important Security Notes:**

- ✅ **DO**: Use environment variables for API keys
- ✅ **DO**: Add API key files to `.gitignore`
- ❌ **DON'T**: Hardcode API keys in your code
- ❌ **DON'T**: Commit API keys to version control

### Getting Your API Key

1. Log in to [Abacus.AI](https://abacus.ai)
2. Navigate to your account settings
3. Find the API Keys section
4. Generate a new API key or copy an existing one
5. Set it as an environment variable (see Installation section)

## 🛠️ Advanced Usage

### Custom LLM Models

```python
# Use a specific LLM model
result = summarizer.summarize_pdf(
    pdf_path='document.pdf',
    llm_name='gpt-4',  # Specify your preferred model
    style='detailed'
)
```

### Batch Processing

```python
from pathlib import Path

# Process all PDFs in a directory
pdf_files = Path('documents/').glob('*.pdf')

for pdf_file in pdf_files:
    result = summarizer.summarize_pdf(pdf_path=str(pdf_file))
    print(f"{pdf_file.name}: {result['summary']}")
```

### Error Handling

```python
try:
    result = summarizer.summarize_pdf(pdf_path='document.pdf')
    print(result['summary'])
except FileNotFoundError:
    print("PDF file not found")
except Exception as e:
    print(f"Error processing PDF: {str(e)}")
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🔗 Resources

- [Abacus.AI Documentation](https://docs.abacus.ai)
- [Abacus.AI Python SDK](https://pypi.org/project/abacusai/)
- [API Reference](https://api.abacus.ai/)

## 💡 Use Cases

- **Research**: Quickly summarize academic papers and research documents
- **Business**: Extract key information from reports and contracts
- **Education**: Create study summaries from textbooks and lecture notes
- **Legal**: Analyze legal documents and extract relevant clauses
- **Content Creation**: Generate content briefs from source materials

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'abacusai'`
- **Solution**: Install the SDK with `pip install abacusai`

**Issue**: `Authentication error` or `Invalid API key`
- **Solution**: Verify your API key is set correctly in the environment variable

**Issue**: `FileNotFoundError` when processing PDF
- **Solution**: Check the file path is correct and the file exists

**Issue**: PDF text extraction returns empty string
- **Solution**: Ensure the PDF contains extractable text (not just images)

## 📧 Support

For questions and support:
- Check the [Abacus.AI Documentation](https://docs.abacus.ai)
- Open an issue in this repository
- Contact Abacus.AI support

## 🎓 Learning Resources

New to Abacus.AI? Start here:
1. Check out `abacus_sdk_easy.ipynb` for SDK basics
2. Explore `notebooks/pdf_demo.ipynb` for PDF processing examples
3. Visit [Abacus.AI Documentation](https://docs.abacus.ai) for comprehensive guides

---

**Made with ❤️ using Abacus.AI**
