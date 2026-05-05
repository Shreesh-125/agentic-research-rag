from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query: str) -> list[dict]:
    response = client.search(
        query=query,
        max_results=2,
        include_raw_content=False
    )
    
    results = []
    for item in response["results"]:
        results.append({
            "title": item["title"],
            "url": item["url"],
            "content": item["content"]
        })
    
    return results