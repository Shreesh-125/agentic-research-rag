from fastapi import FastAPI
from pydantic import BaseModel
from graph.workflow import research_graph
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Multi-Agent Research Assistant",
    description="An AI system that researches and writes reports automatically",
    version="1.0.0"
)

class ResearchRequest(BaseModel):
    question: str

class ResearchResponse(BaseModel):
    question: str
    final_report: str
    sources: list

@app.get("/")
def root():
    return {"status": "running", "message": "Multi-Agent Research Assistant is live"}

@app.post("/research")
def run_research(request: ResearchRequest):
    result = research_graph.invoke({
        "question": request.question
    })
    
    return ResearchResponse(
        question=result["question"],
        final_report=result["final_report"],
        sources=result["sources"]
    )