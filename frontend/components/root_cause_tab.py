import streamlit as st


def show_root_cause_tab(root_cause):

    st.subheader("🧠 Root Cause Hypothesis")

    st.error(
        root_cause["Root Cause"]
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Confidence",
            f'{root_cause["Confidence"]}%'
        )

    with col2:

        st.metric(
            "Affected Module",
            root_cause["Affected Module"]
        )

    st.subheader("📖 Technical Explanation")

    st.info(
        root_cause["Technical Explanation"]
    )

    st.subheader("📚 Supporting Historical Evidence")

    evidence = root_cause.get(
        "Supporting Evidence"
    )

    if evidence:

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Similarity",
                f'{evidence["Similarity"]}%'
            )

        with col2:

            st.success(
                "Retrieved from RAG Knowledge Base"
            )

        st.write("### Historical Bug")

        st.code(
            evidence["Historical Bug"]
        )

    else:

        st.warning(
            "No supporting historical evidence was found."
        )