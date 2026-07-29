import streamlit as st
from utils.pdf_report import generate_pdf_report


def show_report(
    bug_report,
    uploaded_log,
    triage,
    log_analysis,
    root_cause,
    similar_bugs,
    recommendations
):

    pdf = generate_pdf_report(
        bug_report,
        uploaded_log,
        triage,
        log_analysis,
        root_cause,
        similar_bugs,
        recommendations
    )

    st.divider()

    st.download_button(
        label="📄 Download PDF Report",
        data=pdf,
        file_name="Bug_Analysis_Report.pdf",
        mime="application/pdf"
    )