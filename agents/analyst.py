from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOllama(
    model=os.getenv("LLM_MODEL"),
    base_url=os.getenv("OLLAMA_BASE_URL"),
    temperature=0.1
)

def analyst_agent(state: dict) -> dict:
    raw_results = state["raw_results"]
    question = state["question"]

    articles_text = ""
    for i, article in enumerate(raw_results):
        articles_text += f"""
Article {i+1}: {article['title']}
URL: {article['url']}
Content: {article['content']}
---
"""

    messages = [
        SystemMessage(content="""You are a research analyst.
Your job is to read a set of articles and extract the most important facts, 
statistics, insights and key points relevant to the research question.
Be concise but thorough. Always mention which article each fact came from by its number."""),
        HumanMessage(content=f"""Research question: {question}

Here are the articles to analyze:
{articles_text}

Extract the key facts and insights.""")
    ]

    response = llm.invoke(messages)

    return {
        **state,
        "analysis": response.content,
        "sources": [{"title": r["title"], "url": r["url"]} for r in raw_results]
    }