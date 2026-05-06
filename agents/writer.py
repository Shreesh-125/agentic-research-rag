from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model=os.getenv("LLM_MODEL"),
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
)

def writer_agent(state: dict) -> dict:
    question = state["question"]
    analysis = state["analysis"]
    sources = state["sources"]

    sources_text = ""
    for i, source in enumerate(sources):
        sources_text += f"[{i+1}] {source['title']} - {source['url']}\n"

    messages = [
        SystemMessage(content="""You are a professional research writer.
Your job is to write a clear, well-structured research report based on 
the analysis provided. 

Your report must follow this exact structure:
1. A title
2. An executive summary (2-3 sentences)
3. Key Findings (bullet points)
4. Detailed Analysis (2-3 paragraphs)
5. Conclusion (1 paragraph)
6. References (numbered list)

Write in a professional but easy to understand tone."""),
        HumanMessage(content=f"""Research question: {question}

Analysis and key facts:
{analysis}

Sources to cite:
{sources_text}

Write the full research report now.""")
    ]

    response = llm.invoke(messages)

    return {
        **state,
        "final_report": response.content
    }