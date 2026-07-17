import streamlit as st


def show_triage_tab(triage):

    st.subheader("📋 Triage Agent")

    # -------------------------
    # Metrics
    # -------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Severity",
            triage["Severity"]
        )

    with col2:
        st.metric(
            "Priority",
            triage["Priority"]
        )

    with col3:
        st.metric(
            "Confidence",
            f"{triage['Confidence']}%"
        )

    # -------------------------
    # Component
    # -------------------------

    st.markdown("### 🧩 Component")

    st.info(
        triage["Component"]
    )

    # -------------------------
    # AI Reasoning
    # -------------------------

    st.markdown("### 💡 AI Reasoning")

    st.info(
        triage["Reasoning"]
    )