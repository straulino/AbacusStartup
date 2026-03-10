import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function formatDate(date: Date | string): string {
  const d = new Date(date)
  return d.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  })
}

export function formatLeaveType(type: string): string {
  return type.charAt(0) + type.slice(1).toLowerCase().replace('_', ' ')
}

export function formatStatus(status: string): string {
  return status.charAt(0) + status.slice(1).toLowerCase()
}
