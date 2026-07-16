import os
import sys
import streamlit as st

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(PROJECT_ROOT)

from agents.orchestrator import BugAnalysisOrchestrator

from components.header import show_header
from components.sidebar import show_sidebar
from components.bug_form import show_bug_form
from components.triage_tab import show_triage_tab
from components.log_tab import show_log_tab
from components.recommendation_tab import show_recommendation_tab
from components.similar_bug_tab import show_similar_bug_tab
from components.report import show_report

logo = os.path.join(
    PROJECT_ROOT,
    "assets",
    "robot.png"
)

st.set_page_config(
    page_title="AI Smart Bug Analyzer",
    page_icon=logo if os.path.exists(logo) else "🤖",
    layout="wide"
)

show_header(logo)

show_sidebar(logo)

orchestrator = BugAnalysisOrchestrator()

description, log_contents = show_bug_form()

if st.button(
    "🤖 Analyze with AI",
    use_container_width=True
):

    # Require at least one input
    if description.strip() == "" and log_contents.strip() == "":
        st.error("Please either paste a bug report or upload a log file.")
        st.stop()

    # If only a log is uploaded, use it as the bug text
    bug_text = description if description.strip() else log_contents

    with st.spinner("Analyzing Bug..."):

        results = orchestrator.analyze(
            bug_text,
            log_contents
        )

    triage = results["Triage"]
    log = results["Log Analysis"]

    triage = results["Triage"]

    log = results["Log Analysis"]

    st.divider()

    st.header(
        "🤖 AI Analysis"
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📋 Triage",
            "🔍 Log Analysis",
            "💡 Recommendations",
            "📚 Similar Bugs"
        ]
    )

    with tab1:

        show_triage_tab(
            triage
        )

    with tab2:

        show_log_tab(
            log
        )

    with tab3:

      show_recommendation_tab(
        results["Recommendations"]
    )

    with tab4:

        show_similar_bug_tab()

    show_report(
        triage,
        log
    )