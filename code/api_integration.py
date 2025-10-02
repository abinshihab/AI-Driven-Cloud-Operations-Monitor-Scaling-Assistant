"""
api_integration.py
Handles API calls to OpenAI
"""

import openai

def call_api(prompt):
    """Call OpenAI API and return the response"""
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message.content.strip()
