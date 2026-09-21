import streamlit as st
import requests

API_URL = "http://api:8000/research"

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Multi-Agent Research Assistant")
st.markdown("*Powered by LangGraph + Ollama + Tavily*")
st.divider()

with st.sidebar:
    st.header("ℹ️ How it works")
    st.markdown("""
    1. 🧠 **Planner** breaks your question into search queries
    2. 🔍 **Researcher** searches the web for articles
    3. 📊 **Analyst** extracts key facts from articles
    4. ✍️ **Writer** produces a cited research report
    """)
    st.divider()
    st.markdown("**Model:** phi3:mini (local)")
    st.markdown("**Search:** Tavily API")
    st.markdown("**Orchestration:** LangGraph")

question = st.text_input(
    "Enter your research question:",
    placeholder="e.g. What is the impact of AI on healthcare?",
    key="question_input"
)

if st.button("🚀 Research", type="primary", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a research question first.")
    else:
        with st.status("🤖 Agents are working...", expanded=True) as status:
            st.write("🧠 Planner is breaking down your question...")
            st.write("🔍 Researcher is searching the web...")
            st.write("📊 Analyst is extracting key facts...")
            st.write("✍️ Writer is composing your report...")
            
            try:
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=300
                )
                
                if response.status_code == 200:
                    data = response.json()
                    status.update(
                        label="✅ Research complete!",
                        state="complete"
                    )
                    
                    st.subheader("📄 Research Report")
                    st.markdown(data["final_report"])
                    
                    st.divider()
                    st.subheader("📚 Sources")
                    for i, source in enumerate(data["sources"]):
                        st.markdown(f"{i+1}. [{source['title']}]({source['url']})")
                
                else:
                    status.update(label="❌ Something went wrong", state="error")
                    st.error(f"API returned error: {response.status_code}")
                    
            except requests.exceptions.Timeout:
                status.update(label="❌ Request timed out", state="error")
                st.error("The research took too long. Please try again.")
            except Exception as e:
                status.update(label="❌ Error occurred", state="error")
                st.error(f"Error: {str(e)}")