from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os
import json

load_dotenv()

llm = ChatGroq(
    model=os.getenv("LLM_MODEL"),
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)

def planner_agent(state: dict) -> dict:
    question = state["question"]

    messages = [
        SystemMessage(content="""You are a research planner. 
Your job is to break down a research question into exactly 2 focused search queries.
You must respond with ONLY a JSON array of 2 strings. No explanation. No extra text.
Example: ["query one", "query two"]"""),
        HumanMessage(content=f"Research question: {question}")
    ]

    response = llm.invoke(messages)
    
    raw = response.content.strip()
    
    start = raw.find("[")
    end = raw.rfind("]") + 1
    
    if start == -1 or end == 0:
        search_queries = [question]
    else:
        json_str = raw[start:end]
        try:
            search_queries = json.loads(json_str)
        except Exception:
            lines = [l.strip().strip('"-,') for l in raw.split("\n") if l.strip()]
            search_queries = [l for l in lines if len(l) > 5][:2]

    return {
        **state,
        "search_queries": search_queries
    }