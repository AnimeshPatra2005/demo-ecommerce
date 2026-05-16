"""
Email handling utilities for the e-commerce application.
"""

import re
from typing import Dict, List, Optional


def check_email_format(email: str) -> bool:
    """
    Check if email has valid format with additional checks.
    
    Args:
        email: Email address to check
        
    Returns:
        True if format is valid, False otherwise
    """
    # Basic format check
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return False
    
    # Check for consecutive dots
    if '..' in email:
        return False
    
    # Check domain has at least one dot
    domain = email.split('@')[1]
    if '.' not in domain:
        return False
    
    return True


def normalize_email(email: str) -> str:
    """
    Normalize email address to lowercase.
    
    Args:
        email: Email address to normalize
        
    Returns:
        Normalized email address
    """
    return email.lower().strip()


def extract_domain(email: str) -> Optional[str]:
    """
    Extract domain from email address.
    
    Args:
        email: Email address
        
    Returns:
        Domain name or None if invalid
    """
    try:
        return email.split('@')[1]
    except IndexError:
        return None


def is_corporate_email(email: str) -> bool:
    """
    Check if email is from a corporate domain.
    
    Args:
        email: Email address to check
        
    Returns:
        True if corporate, False otherwise
    """
    free_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    domain = extract_domain(email)
    return domain not in free_domains if domain else False


def format_email_list(emails: List[str]) -> str:
    """
    Format list of emails for display.
    
    Args:
        emails: List of email addresses
        
    Returns:
        Formatted string
    """
    return ', '.join(emails)


def create_email_template(template_type: str, data: Dict) -> str:
    """
    Create email content from template.
    
    Args:
        template_type: Type of email template
        data: Data to fill template
        
    Returns:
        Email content
    """
    templates = {
        'welcome': f"Welcome {data.get('name', 'User')}! Thank you for joining us.",
        'order_confirmation': f"Order #{data.get('order_id')} confirmed. Total: ${data.get('total', 0):.2f}",
        'password_reset': f"Password reset requested for {data.get('email', '')}. Click the link to reset.",
    }
    
    return templates.get(template_type, "")


def validate_email_list(emails: List[str]) -> tuple[List[str], List[str]]:
    """
    Validate a list of email addresses.
    
    Args:
        emails: List of email addresses to validate
        
    Returns:
        Tuple of (valid_emails, invalid_emails)
    """
    valid = []
    invalid = []
    
    for email in emails:
        if check_email_format(email):
            valid.append(email)
        else:
            invalid.append(email)
    
    return valid, invalid

# Made with Bob
