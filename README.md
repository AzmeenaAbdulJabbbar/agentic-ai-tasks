# 🌟 Agentic AI Tasks –

This repository contains my complete hands-on work for mastering **Agentic AI** concepts, tools, and applications. I have successfully completed all the modules and built a real-world **Client Hunting Chatbot** using cutting-edge LLM tools and agentic frameworks.

---

## 📁 Repository Structure & Descriptions

### `00_swarm/`
> ✅ **Swarm Intelligence Algorithms**
- Implemented **Ant Colony Optimization** and **Particle Swarm Optimization** using Python.
- Learned how swarm-based agents can solve optimization problems without centralized control.

---

### `01_uv/`
> ✅ **UV Engine Projects**
- Built agents and logic flows using the **UV (Universal Virtual Machine)** engine.
- Explored virtual agent deployment and multi-agent collaboration in a sandboxed setup.

---

### `02_openrouter/`
> ✅ **OpenRouter API Integration**
- Used OpenRouter to connect with 50+ open-source and free LLMs (e.g., Mixtral, Nous, Pygmalion).
- Learned to configure API keys, rate limits, and OpenAI-compatible SDKs for testing and development.

---

### `03_litellm_openai_agent/`
> ✅ **LiteLLM + OpenAI Agents SDK**
- Integrated **LiteLLM** as a lightweight API gateway for OpenAI-style calls.
- Created basic agents with OpenAI’s **Agents SDK**, and tested custom tool usage.

---

### `04_hello_agent/`
> ✅ **Hello Agent + Multi Tool Setup**
- Basic setup of OpenAI Agents SDK — from `hello_world` to advanced agent flows.
- Developed agents with memory, tool selection, and action chains.

---

### `Chatbot-Online-assistant-/`
> 🧠 **Client Hunting Chatbot (Main Project)**
- Developed a **Client Hunting Chatbot** for online businesses and freelancers.
- Built using:
  - **Chainlit**: for chat interface
  - **Google Gemini API** (or OpenRouter): for LLM responses
  - **LiteLLM**: as backend model switcher
- Use case:
  - Identifies potential clients
  - Generates personalized outreach messages
  - Helps with lead generation strategies
  - Can automate FAQs and product/service explanations

---

## 📚 Learning Outcomes

- ✔️ Practical understanding of **Agentic AI** and autonomous LLM agents.
- ✔️ Integrated multiple tools (LiteLLM, OpenRouter, Gemini, Chainlit) in one ecosystem.
- ✔️ Developed optimization algorithms using **Swarm Intelligence**.
- ✔️ Built a full working chatbot system for real-world **client engagement**.

---

## ⚙️ Installation Guide

> 🔧 Prerequisites:
- Python 3.10+
- `pip`, `venv`
- `.env` file with API keys (OpenRouter / Gemini)

### 🛠️ Setup Steps

```bash
# Clone the repo
git clone https://github.com/AzmeenaAbdulJabbbar/agentic-ai-tasks.git
cd agentic-ai-tasks

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Set your API keys in .env
# For Gemini / OpenRouter / Chainlit / OpenAI
