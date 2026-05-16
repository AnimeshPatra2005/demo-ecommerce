"""
Data formatting utilities for the e-commerce application.
"""

from datetime import datetime
from typing import Any, Dict


def format_currency(amount: float, currency: str = "USD") -> str:
    """
    Format amount as currency.
    
    Args:
        amount: Amount to format
        currency: Currency code
        
    Returns:
        Formatted currency string
    """
    symbols = {
        'USD': '$',
        'EUR': '€',
        'GBP': '£',
        'INR': '₹'
    }
    symbol = symbols.get(currency, '$')
    return f"{symbol}{amount:,.2f}"


def format_date(date: datetime, format_type: str = "short") -> str:
    """
    Format datetime object.
    
    Args:
        date: Datetime to format
        format_type: Format type (short, long, iso)
        
    Returns:
        Formatted date string
    """
    formats = {
        'short': '%m/%d/%Y',
        'long': '%B %d, %Y',
        'iso': '%Y-%m-%d',
        'datetime': '%Y-%m-%d %H:%M:%S'
    }
    return date.strftime(formats.get(format_type, formats['short']))


def format_phone(phone: str) -> str:
    """
    Format phone number for display.
    
    Args:
        phone: Phone number to format
        
    Returns:
        Formatted phone number
    """
    # Remove all non-digits
    digits = ''.join(filter(str.isdigit, phone))
    
    # Format as (XXX) XXX-XXXX for 10 digits
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    
    return phone


def format_name(first_name: str, last_name: str) -> str:
    """
    Format full name.
    
    Args:
        first_name: First name
        last_name: Last name
        
    Returns:
        Formatted full name
    """
    return f"{first_name.strip().title()} {last_name.strip().title()}"


def format_address(address: Dict[str, str]) -> str:
    """
    Format address for display.
    
    Args:
        address: Address dictionary
        
    Returns:
        Formatted address string
    """
    parts = [
        address.get('street', ''),
        address.get('city', ''),
        f"{address.get('state', '')} {address.get('zip', '')}",
        address.get('country', '')
    ]
    return ', '.join(filter(None, parts))


def truncate_text(text: str, max_length: int = 50) -> str:
    """
    Truncate text to maximum length.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        
    Returns:
        Truncated text with ellipsis if needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + '...'


def format_percentage(value: float) -> str:
    """
    Format value as percentage.
    
    Args:
        value: Value to format (0-1 range)
        
    Returns:
        Formatted percentage string
    """
    return f"{value * 100:.1f}%"


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human-readable format.
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        Formatted size string
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"

# Made with Bob
