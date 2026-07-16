import os
import streamlit as st


def show_sidebar(logo):

    with st.sidebar:

        if os.path.exists(logo):

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

        st.write("Backend")
        st.info("Python")

        st.write("Frontend")
        st.info("Streamlit")

        st.write("Active Agents")
        st.info("Triage + Log Analysis")

        st.divider()

        st.caption("Version 2.0")

        st.caption("Infosys Springboard Internship")