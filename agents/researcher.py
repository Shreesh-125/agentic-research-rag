from tools.search import search_web

def researcher_agent(state: dict) -> dict:
    search_queries = state["search_queries"]
    
    all_results = []
    
    for query in search_queries:
        print(f"🔍 Searching: {query}")
        results = search_web(query)
        all_results.extend(results)
    
    return {
        **state,
        "raw_results": all_results
    }