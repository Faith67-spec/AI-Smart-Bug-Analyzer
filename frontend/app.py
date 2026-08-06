import os
import sys
import streamlit as st

# =====================================================
# Project Root
# =====================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(PROJECT_ROOT)

# =====================================================
# Imports
# =====================================================

from agents.orchestrator import BugAnalysisOrchestrator
from rag.knowledge_base_growth import KnowledgeBaseGrowth

from analytics.analytics_store import AnalyticsStore
from analytics.analytics_dashboard import show_analytics_dashboard

from components.header import show_header
from components.sidebar import show_sidebar
from components.bug_form import show_bug_form

from components.triage_tab import show_triage_tab
from components.log_tab import show_log_tab
from components.recommendation_tab import show_recommendation_tab
from components.root_cause_tab import show_root_cause_tab
from components.similar_bug_tab import show_similar_bug_tab
from components.report import show_report

# =====================================================
# Services
# =====================================================

analytics_store = AnalyticsStore()

kb_growth = KnowledgeBaseGrowth()

orchestrator = BugAnalysisOrchestrator()

# =====================================================
# Streamlit Config
# =====================================================

logo = os.path.join(
    PROJECT_ROOT,
    "assets",
    "robot.png"
)

st.set_page_config(

    page_title="Creation of Intelligent Bug Diagnosis Platform with Fix Recommendation Assistance",

    page_icon=logo if os.path.exists(logo) else "🤖",

    layout="wide"

)

# =====================================================
# Navigation
# =====================================================

page = st.sidebar.radio(

    "Navigation",

    [

        "🤖 AI Bug Analyzer",

        "📊 Analytics Dashboard"

    ]

)

if page == "📊 Analytics Dashboard":

    show_analytics_dashboard()

    st.stop()

# =====================================================
# UI
# =====================================================

show_header(logo)

show_sidebar(logo)

description, log_contents = show_bug_form()

# =====================================================
# Analyze Button
# =====================================================

if st.button(

    "🤖 Analyze with AI",

    use_container_width=True

):

    if description.strip() == "" and log_contents.strip() == "":

        st.error(
            "Please either paste a bug report or upload a log file."
        )

        st.stop()

    bug_text = (
        description
        if description.strip()
        else log_contents
    )

    with st.spinner("Analyzing Bug..."):

        results = orchestrator.analyze(

            bug_text,

            log_contents

        )

    # ===========================================
    # Save Results
    # ===========================================

    st.session_state["bug_text"] = bug_text

    st.session_state["log_contents"] = log_contents

    st.session_state["triage"] = results["Triage"]

    st.session_state["log"] = results["Log Analysis"]

    st.session_state["recommendations"] = results["Recommendations"]

    st.session_state["root_cause"] = results["Root Cause"]

    st.session_state["similar_bugs"] = results["Similar Bugs"]

    # ===========================================
    # Analytics Storage
    # ===========================================

    analytics_store.save_analysis(

        {

            "Exception": results["Log Analysis"].get(

                "Exception Type",

                "Unknown"

            ),

            "Severity": results["Triage"].get(

                "Severity",

                "Unknown"

            ),

            "Root Cause": results["Root Cause"].get(

                "Root Cause",

                "Unknown"

            ),

            "Component": results["Root Cause"].get(

                "Affected Module",

                "Unknown"

            ),

            "Confidence": results["Root Cause"].get(

                "Confidence",

                0

            )

        }

    )

   ## st.rerun()
    # =====================================================
# Display Results
# =====================================================

if "triage" in st.session_state:

    bug_text = st.session_state["bug_text"]

    log_contents = st.session_state["log_contents"]

    triage = st.session_state["triage"]

    log = st.session_state["log"]

    recommendations = st.session_state["recommendations"]

    root_cause = st.session_state["root_cause"]

    similar_bugs = st.session_state["similar_bugs"]

    st.divider()

    st.header("🤖 AI Analysis")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(

        [

            "📋 Triage",

            "🔍 Log Analysis",

            "💡 Recommendations",

            "🧠 Root Cause",

            "📚 Similar Bugs"

        ]

    )

    # ======================================
    # Triage
    # ======================================

    with tab1:

        show_triage_tab(
            triage
        )

    # ======================================
    # Log Analysis
    # ======================================

    with tab2:

        show_log_tab(
            log
        )

    # ======================================
    # Recommendations
    # ======================================

    with tab3:

        show_recommendation_tab(
            recommendations
        )

    # ======================================
    # Root Cause
    # ======================================

    with tab4:

        show_root_cause_tab(
            root_cause
        )

    # ======================================
    # Similar Bugs
    # ======================================

    with tab5:

        show_similar_bug_tab(
            similar_bugs
        )

    # ======================================
    # PDF Report
    # ======================================

    show_report(

        bug_text,

        log_contents,

        triage,

        log,

        root_cause,

        similar_bugs,

        recommendations

    )

    # ======================================
    # Knowledge Base Growth
    # ======================================

    st.divider()

    st.subheader(
        "📚 Knowledge Base Growth"
    )

    st.write(
        "Store this verified bug and its resolution so that future analyses can retrieve it through semantic search."
    )

    if st.button(

        "✔ Add Resolved Bug to Knowledge Base",

        use_container_width=True

    ):

        try:

            kb_growth.add_resolved_bug(

                bug_report=bug_text,

                severity=triage.get(

                    "Severity",

                    "Unknown"

                ),

                component=root_cause.get(

                    "Affected Module",

                    "Unknown"

                ),

                root_cause=root_cause.get(

                    "Root Cause",

                    "Unknown"

                ),

                confidence=root_cause.get(

                    "Confidence",

                    0

                ),

                recommendations="\n".join(
                    recommendations
                )

            )

            st.success(

                "✅ Bug successfully added to the knowledge base.\n\n"
                "Future analyses can retrieve this resolved defect."

            )

        except Exception as e:

            st.error(

                f"Knowledge Base Update Failed:\n\n{e}"

            )
