import pandas as pd
import streamlit as st

from analytics.analytics_store import AnalyticsStore


def show_analytics_dashboard():

    store = AnalyticsStore()

    analyses = store.get_all_analyses()

    st.header("📊 Defect Pattern Analytics Dashboard")

    if len(analyses) == 0:

        st.info("No bug analyses available yet.")

        return

    df = pd.DataFrame(analyses)

    total_bugs = len(df)

    avg_confidence = round(df["Confidence"].mean(), 1)

    top_exception = df["Exception"].mode()[0]

    top_component = df["Component"].mode()[0]

    top_root_cause = df["Root Cause"].mode()[0]

    # ===============================
    # Summary Metrics
    # ===============================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Bugs",
            total_bugs
        )

    with col2:

        st.metric(
            "Average Confidence",
            f"{avg_confidence}%"
        )

    with col3:

        st.metric(
            "Top Exception",
            top_exception
        )

    col4, col5 = st.columns(2)

    with col4:

        st.metric(
            "Top Component",
            top_component
        )

    with col5:

        st.metric(
            "Top Root Cause",
            top_root_cause
        )

    # ===============================
    # AI Insights
    # ===============================

    st.divider()

    st.subheader("🔍 AI Insights")

    high_severity = len(
        df[
            df["Severity"].str.lower().isin(
                ["high", "critical"]
            )
        ]
    )

    st.info(
        f"""
• **{top_component}** is currently the most frequently affected component.

• **{top_exception}** is the most commonly occurring exception.

• **{top_root_cause}** is the most frequently identified root cause.

• The AI has analysed **{total_bugs}** bug submissions with an average confidence of **{avg_confidence}%**.

• **{high_severity}** high-severity defects have been identified so far.
"""
    )

    # ===============================
    # Charts
    # ===============================

    st.divider()

    st.subheader("📈 Severity Distribution")

    st.bar_chart(
        df["Severity"].value_counts()
    )

    st.subheader("📈 Most Affected Components")

    st.bar_chart(
        df["Component"].value_counts()
    )

    st.subheader("📈 Most Common Root Causes")

    st.bar_chart(
        df["Root Cause"].value_counts()
    )

    # ===============================
    # Recent Analyses
    # ===============================

    st.subheader("📋 Recent Bug Analyses")

    st.dataframe(
        df,
        use_container_width=True
    )