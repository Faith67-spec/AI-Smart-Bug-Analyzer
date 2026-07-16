import streamlit as st


def show_log_tab(log):

    st.subheader("🔍 Log Analysis")

    st.write("### Exception Type")

    st.code(log["Exception Type"])

    st.write("### Failure Point")

    st.code(log["Failure Point"])

    st.write("### Affected Code Path")

    if len(log["Affected Code Path"]) > 0:

        for item in log["Affected Code Path"]:

            st.write(f"• {item}")

    else:

        st.info("No stack trace detected.")

    st.subheader("🛠 Likely Cause")

    st.warning(
        log["Likely Cause"]
    )