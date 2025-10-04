"""
AI-Driven Cloud Operations Monitor & Scaling Assistant – Day 3 UI Prototype
Enhanced Gradio interface with full conversation history
"""

import os
import time
import openai
import gradio as gr
from dotenv import load_dotenv

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv("OPENAI_API_KEY.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please check OPENAI_API_KEY.env file.")

# -----------------------------
# Configuration
# -----------------------------
MODEL = "gpt-4o"
MAX_TOKENS = 500
MAX_ATTEMPTS = 3

# -----------------------------
# Storage
# -----------------------------
conversation_history = []
cache = {}

# -----------------------------
# Helper Functions
# -----------------------------
def make_cache_key(prompt, history, context_size=3):
    snippet = "".join([m["content"] for m in history[-context_size:]])
    return f"{prompt}|{snippet}"

def call_llm_api(prompt, history):
    cache_key = make_cache_key(prompt, history)
    if cache_key in cache:
        return cache[cache_key]

    messages = history.copy()
    messages.append({"role": "user", "content": prompt})

    backoff = 1
    for attempt in range(MAX_ATTEMPTS):
        try:
            response = openai.chat.completions.create(
                model=MODEL,
                messages=messages,
                max_tokens=MAX_TOKENS
            )
            assistant_reply = response.choices[0].message.content.strip()
            cache[cache_key] = assistant_reply
            return assistant_reply

        except openai.RateLimitError:
            time.sleep(backoff)
            backoff *= 2
        except openai.APIError as e:
            time.sleep(backoff)
            backoff *= 2
        except openai.OpenAIError as e:
            break
        except Exception as e:
            break

    return "Sorry, the cloud assistant is temporarily unavailable. Please try again."

# -----------------------------
# Initialize system instruction
# -----------------------------
conversation_history.append({
    "role": "system",
    "content": (
        "You are an AI Cloud Operations Monitor & Scaling Assistant. "
        "You help manage cloud resources, monitor performance, and provide scaling suggestions. "
        "Answer as an expert cloud engineer."
    )
})

# -----------------------------
# Gradio interface function
# -----------------------------
def ask_assistant(user_input):
    conversation_history.append({"role": "user", "content": user_input})
    response = call_llm_api(user_input, conversation_history)
    conversation_history.append({"role": "assistant", "content": response})

    # Build full conversation string for display
    full_history = ""
    for msg in conversation_history[1:]:  # skip system instruction
        role = "You" if msg["role"] == "user" else "Assistant"
        full_history += f"{role}: {msg['content']}\n\n"
    return full_history.strip()

# -----------------------------
# Gradio Interface
# -----------------------------
iface = gr.Interface(
    fn=ask_assistant,
    inputs=gr.Textbox(lines=2, placeholder="Ask your cloud assistant..."),
    outputs=gr.Textbox(lines=20, placeholder="Conversation will appear here...", interactive=False),
    title="AI-Driven Cloud Operations Monitor",
    description="Ask your cloud operations assistant about EC2, RDS, scaling, and other cloud resources."
)

iface.launch()
