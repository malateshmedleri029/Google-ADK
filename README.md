# Hello World Agent — Google ADK

A minimal Hello World AI agent built with [Google Agent Development Kit (ADK)](https://github.com/google/adk-python).

---

## Quick Start

```bash
# 1. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API key to hello_agent/.env
# GOOGLE_API_KEY=your-key-here
# Get a free key at: https://aistudio.google.com/app/apikey

# 4. Run in browser
adk web --port 8000
```

Open **http://localhost:8000**, select `hello_agent`, and start chatting.

---

## Project Structure

```
Google-ADK/
├── hello_agent/
│   ├── agent.py        # Agent definition
│   ├── __init__.py     # Package init
│   ├── .env            # Your API key (add your key here)
│   └── .env.example    # Template
├── requirements.txt    # Dependencies
├── .gitignore
├── README.md
└── BUILD_PLAN.md       # Full step-by-step instructions
```

---

## Run Commands

| Command | What it does |
|---------|-------------|
| `adk run hello_agent` | Interactive CLI chat in terminal |
| `adk web --port 8000` | Web UI at http://localhost:8000 |

---

For full instructions, troubleshooting, and file explanations see [BUILD_PLAN.md](./BUILD_PLAN.md).
