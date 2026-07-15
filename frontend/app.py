import streamlit as st

import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from agents.orchestrator import BugAnalysisOrchestrator

st.title("AI Smart Bug Analyzer")

st.subheader("Bug Submission Module")

description = st.text_area(
    "Paste Bug Report"
)

uploaded_file = st.file_uploader(
    "Upload Stack Trace or Error Log",
    type=["txt", "log"]
)

orchestrator = BugAnalysisOrchestrator()

if st.button("Submit"):

    st.success("Bug Report Submitted")

    st.write("### Bug Report")
    st.write(description)

    log_contents = ""

    if uploaded_file:

        st.write("### Uploaded File")
        st.write(uploaded_file.name)

        log_contents = uploaded_file.read().decode("utf-8")

        st.write("### Uploaded Log")

        st.code(log_contents)

    results = orchestrator.analyze(
        description,
        log_contents
    )

    triage = results["Triage"]

    log = results["Log Analysis"]

    st.header("AI Analysis")

    st.subheader("Triage Agent")

    st.write(f"**Severity:** {triage['Severity']}")

    st.write(f"**Priority:** {triage['Priority']}")

    st.write(f"**Component:** {triage['Component']}")

    st.write(f"**Confidence:** {triage['Confidence']}%")

    st.write("**Reasoning:**")

    for reason in triage["Reasoning"]:

        st.write(f"- {reason}")

    st.subheader("Log Analysis Agent")

    st.write(f"**Exception Type:** {log['Exception Type']}")

    st.write(f"**Failure Point:** {log['Failure Point']}")

    st.write("**Affected Code Path:**")

    for step in log["Affected Code Path"]:

        st.write(f"- {step}")

    st.write(f"**Likely Cause:** {log['Likely Cause']}")

    if uploaded_file:

        st.write("Uploaded File:")
        st.write(uploaded_file.name)

        # Read and display the uploaded file
        log_contents = uploaded_file.read().decode("utf-8")

        st.write("Uploaded Log:")
        st.code(log_contents, language="text")
        