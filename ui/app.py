import streamlit as st
import requests

API_URL = "http://api:8000/research"

st.set_page_config(
    page_title="DeepResearch AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Custom Styling ----------
st.markdown("""
<style>
    .main-title {
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        color: #8b949e;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }

    .agent-card {
        padding: 14px;
        border-radius: 12px;
        background-color: #161b22;
        border: 1px solid #30363d;
        text-align: center;
        min-height: 100px;
    }

    .agent-icon {
        font-size: 1.8rem;
    }

    .agent-name {
        font-weight: 600;
        margin-top: 5px;
    }

    .agent-desc {
        font-size: 0.78rem;
        color: #8b949e;
    }

    .source-card {
        padding: 10px 14px;
        border-left: 3px solid #58a6ff;
        margin-bottom: 8px;
        background-color: #161b22;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)


# ---------- Header ----------
st.markdown(
    '<div class="main-title">🧠 DeepResearch AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Autonomous multi-agent research powered by LangGraph, Ollama & Tavily'
    '</div>',
    unsafe_allow_html=True
)


# ---------- Sidebar ----------
with st.sidebar:

    st.header("⚙️ System")

    st.markdown("""
    **LLM**

    `Phi-3 Mini`

    **Inference**

    `Ollama`

    **Orchestration**

    `LangGraph`

    **Web Search**

    `Tavily`

    **Backend**

    `FastAPI`

    **Frontend**

    `Streamlit`
    """)

    st.divider()

    st.header("🔄 Agent Pipeline")

    st.markdown("""
    🧠 **Planner**  
    Decomposes the research question

    ↓

    🔍 **Researcher**  
    Searches the web

    ↓

    📊 **Analyst**  
    Extracts relevant information

    ↓

    ✍️ **Writer**  
    Synthesizes the final report
    """)

    st.divider()

    st.caption("Local LLM inference • Dockerized deployment")


# ---------- Agent Pipeline ----------
st.subheader("🤖 Multi-Agent Workflow")

cols = st.columns(4)

agents = [
    ("🧠", "Planner", "Task decomposition"),
    ("🔍", "Researcher", "Web retrieval"),
    ("📊", "Analyst", "Evidence synthesis"),
    ("✍️", "Writer", "Report generation"),
]

for col, (icon, name, description) in zip(cols, agents):

    with col:
        st.markdown(
            f"""
            <div class="agent-card">
                <div class="agent-icon">{icon}</div>
                <div class="agent-name">{name}</div>
                <div class="agent-desc">{description}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


st.divider()


# ---------- Research Input ----------
st.subheader("🔎 Start a Research Task")

question = st.text_area(
    "Research question",
    placeholder=(
        "Example: How are small language models being optimized "
        "for edge AI applications?"
    ),
    height=100,
    key="question_input"
)

research = st.button(
    "🚀 Start Autonomous Research",
    type="primary",
    use_container_width=True
)


# ---------- Research Execution ----------
if research:

    if not question.strip():

        st.warning("Please enter a research question.")

    else:

        with st.status(
            "🤖 Research agents are working...",
            expanded=True
        ) as status:

            st.write("🧠 Planner → decomposing research question...")
            st.write("🔍 Researcher → searching the web...")
            st.write("📊 Analyst → synthesizing evidence...")
            st.write("✍️ Writer → generating final report...")

            try:

                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=300
                )

                if response.status_code == 200:

                    data = response.json()

                    status.update(
                        label="✅ Research completed successfully",
                        state="complete",
                        expanded=False
                    )

                    # ---------- Report ----------
                    st.divider()

                    st.subheader("📄 Research Report")

                    st.markdown(data.get("final_report", ""))


                    # ---------- Sources ----------
                    sources = data.get("sources", [])

                    if sources:

                        st.divider()

                        st.subheader(
                            f"📚 Sources ({len(sources)})"
                        )

                        for i, source in enumerate(sources):

                            title = source.get(
                                "title",
                                "Untitled source"
                            )

                            url = source.get("url", "#")

                            st.markdown(
                                f"""
                                <div class="source-card">
                                    <strong>{i + 1}. {title}</strong>
                                    <br>
                                    <a href="{url}" target="_blank">
                                        Open source →
                                    </a>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                else:

                    status.update(
                        label="❌ Research failed",
                        state="error"
                    )

                    st.error(
                        f"API returned HTTP {response.status_code}"
                    )

                    try:
                        st.code(response.text)
                    except Exception:
                        pass


            except requests.exceptions.Timeout:

                status.update(
                    label="⏱️ Research timed out",
                    state="error"
                )

                st.error(
                    "The research process took too long. "
                    "Please try a simpler question."
                )


            except requests.exceptions.ConnectionError:

                status.update(
                    label="🔌 Backend unavailable",
                    state="error"
                )

                st.error(
                    "Could not connect to the research API. "
                    "Make sure the Docker containers are running."
                )


            except Exception as e:

                status.update(
                    label="❌ Unexpected error",
                    state="error"
                )

                st.error(str(e))