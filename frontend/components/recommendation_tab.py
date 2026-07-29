import streamlit as st


def show_recommendation_tab(recommendations):

    st.subheader("💡 Remediation Recommendations")

    st.info(
        "Recommendations are generated using root cause analysis, "
        "historical defect patterns, and software engineering best practices."
    )

    for item in recommendations:

        if item.startswith("Root Cause"):

            st.error(item)

        elif item.startswith("Historical Resolution"):

            st.info(item)

        elif item.startswith("Engineering Best Practice"):

            st.warning(item)

        else:

            st.success(item)

    st.divider()

    st.caption(
        "Recommendations are grounded using historical defects retrieved "
        "from the Eclipse Bugzilla knowledge base."
    )