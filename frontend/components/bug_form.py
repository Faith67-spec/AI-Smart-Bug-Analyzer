import streamlit as st


def show_bug_form():

    st.header("🐞 Bug Submission")

    description = st.text_area(
        "Paste Bug Report",
        height=180,
        placeholder="Paste your bug description here..."
    )

    uploaded_file = st.file_uploader(
        "Upload Stack Trace or Error Log",
        type=["txt", "log"]
    )

    log_contents = ""

    if uploaded_file is not None:

        log_contents = uploaded_file.read().decode(
            "utf-8",
            errors="ignore"
        )

        with st.expander("📄 View Uploaded Log"):

            st.code(
                log_contents,
                language="text"
            )

    return description, log_contents