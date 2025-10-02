# AI-Driven Cloud Operations Monitor & Scaling Assistant

A multi-turn AI assistant to monitor, diagnose, and scale cloud resources (EC2, RDS, autoscaling, etc.) using OpenAI GPT API. This is the **Day 3 prototype** of the AI Application Challenge.

---

## Features

- Multi-turn conversation with context retention
- Cloud monitoring and scaling suggestions
- Handles AWS EC2, RDS, and autoscaling scenarios
- Error handling and API request optimization
- Gradio-based web UI for interactive usage

---

## Tech Stack

- Python 3.11
- OpenAI API (`openai` Python package)
- Gradio for web interface
- `python-dotenv` for environment variables

---

## Installation

1. Clone the repository:

```bash
git clone <your-github-repo-link>
cd <your-project-folder>

2. Create and activate a virtual environment:
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

# Windows (Command Prompt)
```bash
python -m venv venv
venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
# Or manually:
```bash
pip install openai gradio python-dotenv
4. Add your OpenAI API key:
Create a .env file (or OPENAI_API_KEY.env) in the project root:
```bash
OPENAI_API_KEY=sk-your_actual_api_key_here
Usage
Run the Gradio UI:
```bash
python day3_gradio_ui.py
Open the link in your browser (Gradio will show a local URL).
Type questions like:
"Check CPU usage for all EC2 instances in us-east-1"
"Why is my RDS database slow?"
"Scale the worker autoscaling group by 2 nodes"
Project Structure
Day3_Cloud_Monitor/
├── day3_gradio_ui.py      # Gradio interface script
├── day3_cloud_monitor.py  # Core assistant logic
├── OPENAI_API_KEY.env     # Your OpenAI API key
├── requirements.txt       # Project dependencies
└── README.md              # Project overview
Challenges & Notes
Upgraded OpenAI SDK to v1.x syntax (chat.completions.create)
Multi-turn conversation maintained via conversation history
Large output box in Gradio for better readability
License
MIT License 
