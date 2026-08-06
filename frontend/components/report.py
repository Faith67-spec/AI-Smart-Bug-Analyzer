import streamlit as st
st.error("REPORT COMPONENT LOADED")
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
    st.success("Generating NEW PDF...")
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

        label="📄 Download AI Analysis Report (PDF)",

        data=pdf,

        file_name="AI_Smart_Bug_Analysis_Report.pdf",

        mime="application/pdf",

        use_container_width=True

    )