import os
import streamlit as st


def show_header(logo):

    col1, col2 = st.columns([1, 5])

    with col1:

        if os.path.exists(logo):

            st.image(
                logo,
                width=110
            )

    with col2:

        st.title(
            "AI Smart Bug Analyzer"
        )

        st.caption(
            "AI-Powered Multi-Agent Defect Analysis using Retrieval-Augmented Generation (RAG)"
        )

    st.divider()