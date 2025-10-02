"""
cloud_monitor.py
Day 4 AI Challenge - Gradio UI for AI-Driven Cloud Operations
"""

import os
import openai
import gradio as gr
from dotenv import load_dotenv
from measure_response import evaluate_response
from api_integration import call_api

# -----------------------------
# Load OpenAI API key
# -----------------------------
load_dotenv(".env")  # looks for .env in project root
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please check .env file.")

# -----------------------------
# Conversation history
# -----------------------------
conversation_history = []

# -----------------------------
# Gradio function
# -----------------------------
def ask_assistant(user_input):
    conversation_history.append({"role": "user", "content": user_input})
    response = call_api(user_input)
    conversation_history.append({"role": "assistant", "content": response})

    # Build full conversation display
    full_history = ""
    for msg in conversation_history:
        role = "You" if msg["role"] == "user" else "Assistant"
        full_history += f"{role}: {msg['content']}\n\n"
    return full_history.strip()

# -----------------------------
# Launch Gradio interface
# -----------------------------
iface = gr.Interface(
    fn=ask_assistant,
    inputs=gr.Textbox(lines=2, placeholder="Ask your cloud assistant..."),
    outputs=gr.Textbox(lines=20, interactive=False),
    title="AI-Driven Cloud Operations Monitor",
    description="Ask your cloud assistant about EC2, RDS, scaling, and other cloud resources."
)

iface.launch()
"""
cloud_monitor.py
Day 4 AI Challenge - Gradio UI for AI-Driven Cloud Operations
"""

import os
import openai
import gradio as gr
from dotenv import load_dotenv
from measure_response import evaluate_response
from api_integration import call_api

# -----------------------------
# Load OpenAI API key
# -----------------------------
load_dotenv(".env")  # looks for .env in project root
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please check .env file.")

# -----------------------------
# Conversation history
# -----------------------------
conversation_history = []

# -----------------------------
# Gradio function
# -----------------------------
def ask_assistant(user_input):
    conversation_history.append({"role": "user", "content": user_input})
    response = call_api(user_input)
    conversation_history.append({"role": "assistant", "content": response})

    # Build full conversation display
    full_history = ""
    for msg in conversation_history:
        role = "You" if msg["role"] == "user" else "Assistant"
        full_history += f"{role}: {msg['content']}\n\n"
    return full_history.strip()

# -----------------------------
# Launch Gradio interface
# -----------------------------
iface = gr.Interface(
    fn=ask_assistant,
    inputs=gr.Textbox(lines=2, placeholder="Ask your cloud assistant..."),
    outputs=gr.Textbox(lines=20, interactive=False),
    title="AI-Driven Cloud Operations Monitor",
    description="Ask your cloud assistant about EC2, RDS, scaling, and other cloud resources."
)

iface.launch()
