"""
utils.py
Helper functions (text cleaning, preprocessing)
"""

import re

def clean_text(text: str) -> str:
    """Basic text cleaning."""
    if not text:
        return ""
    text = re.sub(r"\s+", " ", text)  # normalize whitespace
    text = text.strip()
    return text
