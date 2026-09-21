import streamlit as st
import requests

API_URL = "http://api:8000/research"

st.set_page_config(
    page_title="DeepResearch AI",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

    /* Main page */
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Header */
    .title {
        font-size: 2.7rem;
        font-weight: 700;
        letter-spacing: -1px;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        font-size: 1.05rem;
        color: #8b949e;
        margin-bottom: 2rem;
    }

    /* Agent cards */
    .agent-card {
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 18px 14px;
        text-align: center;
        background: #161b22;
        min-height: 120px;
    }

    .agent-name {
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 7px;
    }

    .agent-description {
        font-size: 0.8rem;
        color: #8b949e;
        line-height: 1.4;
    }

    /* Source cards */
    .source-card {
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 13px 16px;
        margin-bottom: 10px;
        background: #161b22;
    }

    .source-title {
        font-weight: 600;
        font-size: 0.95rem;
    }

    .source-url {
        font-size: 0.8rem;
        color: #8b949e;
        margin-top: 4px;
    }

    /* Section headers */
    .section-title {
        font-size: 1.35rem;
        font-weight: 650;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        border-right: 1px solid #30363d;
    }

    /* Text area */
    textarea {
        font-size: 1rem !important;
    }

    /* Buttons */
    .stButton > button {
        height: 45px;
        font-weight: 600;
        border-radius: 8px;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="title">DeepResearch AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Autonomous multi-agent research system for web-based research and analysis'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.markdown("## System")

    st.markdown("""
    **Language Model**

    Phi-3 Mini via Ollama

    **Agent Orchestration**

    LangGraph

    **Web Research**

    Tavily Search

    **Backend**

    FastAPI

    **Interface**

    Streamlit
    """)

    st.divider()

    st.markdown("## Architecture")

    st.markdown("""
    **Planner**

    Breaks the research question into focused search queries.

    **Researcher**

    Searches the web and collects relevant sources.

    **Analyst**

    Extracts and synthesizes important information.

    **Writer**

    Produces the final research report.
    """)

    st.divider()

    st.caption("Local LLM inference with Dockerized deployment")


# -----------------------------
# Agent Pipeline
# -----------------------------
st.markdown(
    '<div class="section-title">Multi-Agent Workflow</div>',
    unsafe_allow_html=True
)

columns = st.columns(4)

agents = [
    (
        "Planner",
        "Task decomposition"
    ),
    (
        "Researcher",
        "Web retrieval"
    ),
    (
        "Analyst",
        "Evidence synthesis"
    ),
    (
        "Writer",
        "Report generation"
    )
]

for column, (name, description) in zip(columns, agents):

    with column:

        st.markdown(
            f"""
            <div class="agent-card">
                <div class="agent-name">{name}</div>
                <div class="agent-description">
                    {description}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


st.divider()


# -----------------------------
# Research Input
# -----------------------------
st.markdown(
    '<div class="section-title">🔎 Research</div>',
    unsafe_allow_html=True
)

question = st.text_area(
    "Research Question",
    placeholder=(
        "Enter a question you want the research agents to investigate..."
    ),
    height=110,
    label_visibility="visible"
)

start_research = st.button(
    "Start Research",
    type="primary",
    use_container_width=True
)


# -----------------------------
# Research Execution
# -----------------------------
if start_research:

    if not question.strip():

        st.warning("Please enter a research question.")

    else:

        with st.status(
            "Research in progress...",
            expanded=True
        ) as status:

            st.write("Planner is decomposing the research question.")
            st.write("Researcher is searching the web.")
            st.write("Analyst is synthesizing the retrieved information.")
            st.write("Writer is generating the final report.")

            try:

                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=300
                )

                if response.status_code == 200:

                    data = response.json()

                    status.update(
                        label="Research completed",
                        state="complete",
                        expanded=False
                    )

                    # -----------------------------
                    # Final Report
                    # -----------------------------
                    st.divider()

                    st.markdown(
                        '<div class="section-title">Research Report</div>',
                        unsafe_allow_html=True
                    )

                    final_report = data.get("final_report", "")

                    st.markdown(final_report)


                    # -----------------------------
                    # Sources
                    # -----------------------------
                    sources = data.get("sources", [])

                    if sources:

                        st.divider()

                        st.markdown(
                            f'<div class="section-title">'
                            f'Sources ({len(sources)})'
                            f'</div>',
                            unsafe_allow_html=True
                        )

                        for index, source in enumerate(sources):

                            title = source.get(
                                "title",
                                "Untitled source"
                            )

                            url = source.get(
                                "url",
                                "#"
                            )

                            st.markdown(
                                f"""
                                <div class="source-card">
                                    <div class="source-title">
                                        {index + 1}. {title}
                                    </div>
                                    <div class="source-url">
                                        <a href="{url}" target="_blank">
                                            Open source
                                        </a>
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                else:

                    status.update(
                        label="Research failed",
                        state="error"
                    )

                    st.error(
                        f"API returned HTTP {response.status_code}"
                    )

                    if response.text:
                        st.code(response.text)


            except requests.exceptions.Timeout:

                status.update(
                    label="Research timed out",
                    state="error"
                )

                st.error(
                    "The research process took too long. "
                    "Please try a simpler question."
                )


            except requests.exceptions.ConnectionError:

                status.update(
                    label="Backend unavailable",
                    state="error"
                )

                st.error(
                    "Could not connect to the research API. "
                    "Make sure the Docker containers are running."
                )


            except Exception as error:

                status.update(
                    label="Unexpected error",
                    state="error"
                )

                st.error(str(error))