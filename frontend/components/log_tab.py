import streamlit as st


def show_log_tab(log):

    st.subheader("🔍 Log Analysis Agent")

    # -------------------------
    # Metrics
    # -------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Exception Type",
            log["Exception Type"]
        )

    with col2:
        st.metric(
            "Confidence",
            f"{log['Confidence']}%"
        )

    # -------------------------
    # Failure Point
    # -------------------------

    st.markdown("### 🎯 Failure Point")

    st.info(
        log["Failure Point"]
    )

    # -------------------------
    # Code Path
    # -------------------------

    st.markdown("### 🛤 Affected Code Path")

    if log["Affected Code Path"]:

        for item in log["Affected Code Path"]:

            st.write(f"• {item}")

    else:

        st.info("No stack trace detected.")

    # -------------------------
    # Root Cause
    # -------------------------

    st.markdown("### 🛠 Likely Cause")

    st.warning(
        log["Likely Cause"]
    )