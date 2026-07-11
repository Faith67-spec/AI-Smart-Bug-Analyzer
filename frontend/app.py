import streamlit as st

st.title("AI Smart Bug Analyzer")

st.subheader("Bug Submission Module")

description = st.text_area(
    "Paste Bug Report"
)

uploaded_file = st.file_uploader(
    "Upload Stack Trace or Error Log",
    type=["txt", "log"]
)

if st.button("Submit"):

    st.success("Bug Report Submitted")

    st.write("Description:")
    st.write(description)

    if uploaded_file:

        st.write("Uploaded File:")
        st.write(uploaded_file.name)

        # Read and display the uploaded file
        log_contents = uploaded_file.read().decode("utf-8")

        st.write("Uploaded Log:")
        st.code(log_contents, language="text")
        