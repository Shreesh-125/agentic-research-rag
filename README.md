# 🔬 Multi-Agent Research Assistant

An autonomous AI system where 4 specialized agents collaborate to research any topic and generate a fully cited report — automatically.

---

## 🎯 Problem Statement

Manual research is time-consuming. Finding articles, reading them, extracting facts, and writing a structured report takes 2-4 hours. This system does it in minutes.

---

## 🏗️ Architecture

User Question
↓
[Planner Agent] → Breaks question into 2 focused search queries
↓
[Researcher Agent] → Searches the web using Tavily API
↓
[Analyst Agent] → Extracts key facts from articles using LLM
↓
[Writer Agent] → Produces a fully cited research report
↓
Final Report

## 🤖 Tech Stack

| Layer               | Technology         |
| ------------------- | ------------------ |
| Agent Orchestration | LangGraph          |
| Local LLM           | Ollama + phi3:mini |
| Web Search          | Tavily API         |
| API Layer           | FastAPI            |
| Chat UI             | Streamlit          |
| Containerization    | Docker             |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Docker
- Ollama installed with phi3:mini model
- Tavily API key (free at tavily.com)

### 1. Clone the repository

```bash
git clone https://github.com/basavraj21/multi-agent-researcher.git
cd multi-agent-researcher
```

### 2. Create your .env file

```bash
cp .env.example .env
```

Fill in your Tavily API key in `.env`

### 3. Run with Docker

```bash
docker-compose up --build
```

### 4. Open the UI

http://localhost:8501

---

## 📁 Project Structure

multi-agent-researcher/
│
├── agents/
│ ├── planner.py ← Breaks question into search queries
│ ├── researcher.py ← Searches web using Tavily
│ ├── analyst.py ← Extracts key facts from articles
│ └── writer.py ← Writes final cited report
│
├── graph/
│ └── workflow.py ← LangGraph orchestration
│
├── tools/
│ └── search.py ← Tavily search tool
│
├── api/
│ └── main.py ← FastAPI endpoints
│
├── ui/
│ └── app.py ← Streamlit chat interface
│
├── .env ← API keys (never committed)
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

---

## 🔑 Environment Variables

Create a `.env` file with the following:

TAVILY_API_KEY=your_tavily_api_key
OLLAMA_BASE_URL=http://localhost:11434
LLM_MODEL=phi3:mini

---

## 👤 Author

Basavraj — M.Sc. Data Science & Analytics, SRH University Heidelberg
