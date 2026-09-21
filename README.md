DeepResearch AI

An autonomous multi-agent research system for automated web research, information analysis, and report generation.

DeepResearch AI uses a coordinated multi-agent workflow to transform a research question into a structured, source-backed report.

Overview

Traditional research requires manually searching for sources, reading articles, extracting relevant information, and organizing the findings.

DeepResearch AI automates this workflow using specialized AI agents. Each agent performs a specific stage of the research process, while LangGraph coordinates the overall workflow.

The system uses a locally hosted Phi-3 Mini model through Ollama, combined with Tavily for real-time web search.

Architecture
                         Research Question
                                |
                                v
                       +----------------+
                       |  Planner Agent |
                       +----------------+
                                |
                         Search Queries
                                |
                                v
                     +-------------------+
                     | Researcher Agent  |
                     +-------------------+
                                |
                         Web Sources
                                |
                                v
                       +---------------+
                       | Analyst Agent |
                       +---------------+
                                |
                       Analyzed Findings
                                |
                                v
                       +-------------+
                       | Writer Agent|
                       +-------------+
                                |
                                v
                       +----------------+
                       | Research Report|
                       +----------------+
                                |
                                v
                         Source References
Multi-Agent Workflow
1. Planner Agent

Analyzes the user's research question and decomposes it into focused search queries.

2. Researcher Agent

Executes the generated queries using Tavily and collects relevant web sources.

3. Analyst Agent

Processes the retrieved information using the language model and extracts important facts, findings, and supporting information.

4. Writer Agent

Synthesizes the analyzed information into a structured research report with references to the retrieved sources.

Technology Stack
Component	Technology
Agent Orchestration	LangGraph
Language Model	Phi-3 Mini
Local LLM Runtime	Ollama
Web Search	Tavily
Backend API	FastAPI
Frontend	Streamlit
Containerization	Docker
Language	Python
Project Structure
multi-agent-researcher/
│
├── agents/
│   ├── planner.py
│   ├── researcher.py
│   ├── analyst.py
│   └── writer.py
│
├── graph/
│   └── workflow.py
│
├── tools/
│   └── search.py
│
├── api/
│   └── main.py
│
├── ui/
│   └── app.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
Key Features
Multi-agent research workflow using LangGraph
Automated research question decomposition
Real-time web search using Tavily
Local LLM inference using Ollama
Specialized planning, research, analysis, and writing agents
Structured research report generation
Source references for retrieved information
FastAPI backend
Streamlit web interface
Dockerized application
Getting Started
Prerequisites

Make sure the following are installed:

Docker Desktop
Ollama
Phi-3 Mini
Tavily API key
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/multi-agent-researcher.git
cd multi-agent-researcher

Replace YOUR_USERNAME with your GitHub username.

2. Configure Environment Variables

Create a .env file in the project root:

TAVILY_API_KEY=your_tavily_api_key
OLLAMA_BASE_URL=http://host.docker.internal:11434
LLM_MODEL=phi3:mini

Make sure .env is not committed to Git.

3. Install the Ollama Model

Pull the Phi-3 Mini model:

ollama pull phi3:mini

Verify that the model is available:

ollama list
4. Start the Application

Build and start the Docker containers:

docker compose up --build
5. Open the Application

Open the Streamlit interface:

http://localhost:8501

API Usage

The FastAPI backend exposes the following endpoint:

POST /research

Example request:

curl -X POST http://localhost:8000/research \
  -H "Content-Type: application/json" \
  -d '{"question":"What are the major challenges in deploying small language models on edge devices?"}'

The API returns:

Research question
Generated research report
Retrieved sources
Example Workflow

Given the question:

What are the major challenges in deploying small language models on edge devices?

The system performs the following process:

Research Question
       |
       v
Question Decomposition
       |
       v
Web Search
       |
       v
Information Analysis
       |
       v
Report Generation
       |
       v
Sources + Final Report
Design Principles
Specialized Agents

Each agent is responsible for a specific stage of the research workflow instead of relying on a single LLM call.

Local Inference

The system uses Ollama to run Phi-3 Mini locally, reducing dependence on hosted LLM inference for the core generation process.

Modular Architecture

Agents, tools, API components, and the LangGraph workflow are separated into independent modules, making the system easier to extend.

Reproducible Deployment

Docker is used to provide a consistent runtime environment for the backend and frontend components.

Future Improvements

Potential extensions include:

Retrieval-Augmented Generation
Persistent research memory
Source quality evaluation
Iterative research and query refinement
Parallel research agents
Research history and report storage
Support for additional local and hosted LLMs
Author

Shreesh Polawar