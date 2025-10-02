"""
measure_response.py
Day 4 AI Challenge - Performance & Evaluation of Cloud Assistant Responses
"""

import os
import sys
from dotenv import load_dotenv
from api_integration import call_api

# -----------------------------
# Load OpenAI API key
# -----------------------------
# Project root (one level above /code)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
env_path = os.path.join(PROJECT_ROOT, ".env")

if not os.path.exists(env_path):
    sys.exit(f"❌ .env not found at {env_path}. Please create it with OPENAI_API_KEY.")

load_dotenv(dotenv_path=env_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    sys.exit("❌ OpenAI API key not found in .env")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY  # ensure OpenAI sees it

# -----------------------------
# Evaluation function
# -----------------------------
def evaluate_response(prompt):
    """
    Call the API with a prompt and return the response with basic metrics.
    """
    try:
        response = call_api(prompt)
    except Exception as e:
        return f"⚠️ Error calling API: {str(e)}"

    # Basic evaluation metrics (you can expand later)
    evaluation = {
        "response_text": response,
        "length": len(response),
        "word_count": len(response.split())
    }

    return evaluation

# -----------------------------
# Test block
# -----------------------------
if __name__ == "__main__":
    test_prompt = "How can I monitor EC2 instances efficiently in AWS?"
    result = evaluate_response(test_prompt)
    print("Evaluation Result:")
    print(result)
