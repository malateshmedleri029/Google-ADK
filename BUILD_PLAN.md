# Build Plan: Hello World Agent (Google ADK)

Complete guide from project setup to running in the browser.

---

## Project Structure

```
Google-ADK/
├── hello_agent/
│   ├── __init__.py       # Package init — imports agent module
│   ├── agent.py          # Agent definition with root_agent
│   ├── .env              # Your Google API key (never commit this)
│   └── .env.example      # Template for .env
├── requirements.txt      # Python dependencies
├── .gitignore            # Excludes .env and .venv from git
├── README.md             # Quick start guide
└── BUILD_PLAN.md         # This file
```

---

## Prerequisites

- Python 3.10 or later (recommended — 3.9 works but shows deprecation warnings)
- pip (Python package manager)
- A Google API key — get one free at https://aistudio.google.com/app/apikey

---

## Phase 1: Setup

### Step 1 — Create and activate virtual environment

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (CMD):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

> Run this every time you open a new terminal session.

---

### Step 2 — Install dependencies

```bash
pip install -r requirements.txt
```

**What gets installed:**

| Package | Purpose |
|---------|---------|
| `google-adk` | Google Agent Development Kit — agent runtime, CLI, web UI |
| `python-multipart` | Required for the ADK web UI to load correctly (file upload routes) |

> **Note:** If you skip `python-multipart`, the web UI will start but crash silently and the chat interface will not appear.

---

### Step 3 — Configure your API key

Open `hello_agent/.env` and add your key:

```
GOOGLE_API_KEY=your-actual-api-key-here
```

Get a free key at: https://aistudio.google.com/app/apikey

> `.env` is listed in `.gitignore` — it will never be committed to git.

---

## Phase 2: Project Files Explained

### `hello_agent/agent.py`

```python
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="hello_agent",
    description="A simple Hello World agent.",
    instruction="You are a friendly assistant. Greet users and respond briefly.",
)
```

| Field | Purpose |
|-------|---------|
| `root_agent` | Required variable name — ADK discovers the agent by this name |
| `Agent` | LLM-powered agent class from ADK |
| `model` | Gemini model to use (`gemini-2.5-flash` is fast and free-tier friendly) |
| `name` | Identifier shown in logs and the web UI |
| `description` | Short summary of what the agent does |
| `instruction` | System prompt — defines the agent's personality and behaviour |

---

### `hello_agent/__init__.py`

```python
from . import agent
```

Makes `hello_agent` a Python package and ensures `root_agent` is loaded when ADK starts.

---

### `hello_agent/.env`

```
GOOGLE_API_KEY=your-api-key-here
```

ADK loads this file automatically. Never share or commit this file.

---

### `hello_agent/.env.example`

```
GOOGLE_API_KEY=your-api-key-here
```

Safe-to-commit template. Copy to `.env` and add your real key.

---

### `requirements.txt`

```
google-adk>=0.1.0
python-multipart>=0.0.9
```

Install with: `pip install -r requirements.txt`

---

### `.gitignore`

Excludes `.env`, `.venv/`, and Python cache files from version control.

---

## Phase 3: Run the Agent

### Option A — CLI chat (terminal)

```bash
adk run hello_agent
```

- Type a message and press Enter
- Type `exit` to quit

---

### Option B — Web UI in browser

```bash
adk web --port 8000
```

Then open your browser at: **http://localhost:8000**

1. Select **`hello_agent`** from the dropdown (top-left)
2. Type a message in the input box
3. Press Enter — the agent responds

> Run this command from the project root directory (the folder containing `hello_agent/`).

---

## Phase 4: Checklist

- [x] Virtual environment created and activated
- [x] `pip install -r requirements.txt` completed
- [x] `python-multipart` installed (required for web UI)
- [x] API key added to `hello_agent/.env`
- [x] `adk run hello_agent` — CLI chat works
- [x] `adk web --port 8000` — Web UI loads at http://localhost:8000
- [x] Agent responds to messages in the browser

---

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Web UI shows blank / no chat | `python-multipart` missing | `pip install python-multipart` |
| `adk: command not found` | Virtual environment not active | Run `source .venv/bin/activate` |
| API errors when chatting | Invalid or missing API key | Check `hello_agent/.env` has a valid key |
| `ModuleNotFoundError: google.adk` | Dependencies not installed | Run `pip install -r requirements.txt` |
| Python deprecation warnings | Using Python 3.9 (ADK needs 3.10+) | Upgrade Python to 3.10 or later |
| Port 8000 already in use | Another process using port 8000 | Use `adk web --port 8001` and open http://localhost:8001 |

---

## Quick Reference — All Commands

```bash
# 1. Activate virtual environment (every new terminal session)
source .venv/bin/activate          # macOS/Linux
# .venv\Scripts\activate.bat       # Windows CMD
# .venv\Scripts\Activate.ps1       # Windows PowerShell

# 2. Install dependencies (one-time)
pip install -r requirements.txt

# 3. Run CLI chat
adk run hello_agent

# 4. Run Web UI (browser at http://localhost:8000)
adk web --port 8000
```
