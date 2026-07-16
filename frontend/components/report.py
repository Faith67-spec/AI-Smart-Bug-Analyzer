import streamlit as st


def show_report(triage, log):

    report = f"""
AI SMART BUG ANALYZER REPORT

Severity: {triage['Severity']}
Priority: {triage['Priority']}
Confidence: {triage['Confidence']}%

Component:
{triage['Component']}

Exception:
{log['Exception Type']}

Failure Point:
{log['Failure Point']}

Likely Cause:
{log['Likely Cause']}
"""

    st.divider()

    st.download_button(

        "📄 Download Report",

        report,

        file_name="bug_analysis_report.txt",

        mime="text/plain"

    )