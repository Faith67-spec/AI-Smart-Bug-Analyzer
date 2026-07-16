import streamlit as st


def show_triage_tab(triage):

    st.subheader("📋 Triage Agent")

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

    st.write("### 🧩 Component")

    st.info(
        triage["Component"]
    )

    st.subheader("💡 AI Reasoning")

    for reason in triage["Reasoning"]:

        st.success(reason)