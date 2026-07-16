import streamlit as st
import os
import sys

# -----------------------------
# Project Path
# -----------------------------
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from agents.orchestrator import BugAnalysisOrchestrator

# -----------------------------
# Assets
# -----------------------------
logo = os.path.join(
    os.path.dirname(__file__),
    "..",
    "assets",
    "robot.png"
)

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Smart Bug Analyzer",
    page_icon=logo,
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
col1, col2 = st.columns([1, 5])

with col1:
    st.image(
        logo,
        width=120
    )

with col2:
    st.title("AI Smart Bug Analyzer")
    st.caption(
        "AI-Powered Multi-Agent Defect Analysis using Retrieval-Augmented Generation (RAG)"
    )

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.image(
        logo,
        width=80
    )

    st.header("Project Information")

    st.success("Status: Active")

    st.write("Embedding Model")
    st.info("all-MiniLM-L6-v2")

    st.write("Vector Database")
    st.info("ChromaDB")

    st.write("Framework")
    st.info("Streamlit + Python")

    st.write("Active Agents")
    st.info("2 (Triage + Log Analysis)")

# -----------------------------
# Input Section
# -----------------------------
st.subheader("🐞 Submit a Bug")

description = st.text_area(
    "Paste Bug Report"
)

uploaded_file = st.file_uploader(
    "Upload Stack Trace or Error Log",
    type=["txt", "log"]
)

# -----------------------------
# Initialize AI
# -----------------------------
orchestrator = BugAnalysisOrchestrator()

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("🤖 Analyze with AI"):

    st.success("Bug Report Submitted Successfully")

    log_contents = ""

    st.write("### 📝 Bug Report")
    st.write(description)

    if uploaded_file:

        st.write("### 📄 Uploaded File")
        st.write(uploaded_file.name)

        log_contents = uploaded_file.read().decode("utf-8")

        with st.expander("📄 View Uploaded Log"):
            st.code(
                log_contents,
                language="text"
            )

    # -----------------------------
    # AI Processing
    # -----------------------------
    results = orchestrator.analyze(
        description,
        log_contents
    )

    triage = results["Triage"]
    log = results["Log Analysis"]

    # -----------------------------
    # Results
    # -----------------------------
    st.divider()

    st.header("🤖 AI Analysis")

    st.subheader("📋 Triage Agent")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Severity",
            triage["Severity"]
        )

    with col2:
        st.metric(
            "Priority",
            triage["Priority"]
        )

    with col3:
        st.metric(
            "Confidence",
            f"{triage['Confidence']}%"
        )

    st.write("### 🧩 Affected Component")
    st.info(triage["Component"])

    st.subheader("💡 AI Reasoning")

    for reason in triage["Reasoning"]:
        st.success(reason)

    st.divider()

    st.subheader("🔍 Log Analysis Agent")

    st.write("**Exception Type**")
    st.code(log["Exception Type"])

    st.write("**Failure Point**")
    st.code(log["Failure Point"])

    st.write("**Affected Code Path**")

    if len(log["Affected Code Path"]) > 0:

        for step in log["Affected Code Path"]:
            st.write(f"• {step}")

    else:

        st.info("No stack trace found.")

    st.subheader("🛠 Likely Cause")
    st.warning(log["Likely Cause"])