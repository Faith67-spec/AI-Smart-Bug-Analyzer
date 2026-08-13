import pandas as pd
import streamlit as st

from analytics.analytics_store import AnalyticsStore


def get_top_real_value(series, placeholders):
    """
    Return the most frequent meaningful value while ignoring
    placeholder values such as Unknown or N/A.
    """

    valid = series.dropna().astype(str).str.strip()

    placeholder_values = [
        str(value).strip().lower()
        for value in placeholders
    ]

    valid = valid[
        ~valid.str.lower().isin(placeholder_values)
    ]

    if len(valid) == 0:
        return "No identified pattern"

    return valid.mode().iloc[0]


def show_analytics_dashboard():

    store = AnalyticsStore()

    analyses = store.get_all_analyses()

    st.header("📊 Defect Pattern Analytics Dashboard")

    if len(analyses) == 0:

        st.info("No bug analyses available yet.")

        return

    df = pd.DataFrame(analyses)

    # ===============================
    # Summary Calculations
    # ===============================

    total_bugs = len(df)

    # Make sure Confidence is numeric
    df["Confidence"] = pd.to_numeric(
        df["Confidence"],
        errors="coerce"
    )

    avg_confidence = round(
        df["Confidence"].mean(),
        1
    )

    # ===============================
    # Identify Top Patterns
    # ===============================

    top_exception = get_top_real_value(
        df["Exception"],
        [
            "unknown",
            "none",
            "n/a",
            "nan"
        ]
    )

    top_component = get_top_real_value(
        df["Component"],
        [
            "unknown",
            "none",
            "n/a",
            "nan"
        ]
    )

    top_root_cause = get_top_real_value(
        df["Root Cause"],
        [
            "unknown",
            "none",
            "n/a",
            "nan",
            "unable to determine the exact cause."
        ]
    )

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

    # Safely handle missing/empty severity values
    severity_values = (
        df["Severity"]
        .fillna("")
        .astype(str)
        .str.lower()
        .str.strip()
    )

    high_severity = len(
        df[
            severity_values.isin(
                [
                    "high",
                    "critical"
                ]
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

    # -------------------------------
    # Severity Distribution
    # -------------------------------

    st.subheader("📈 Severity Distribution")

    severity_chart = (
        df["Severity"]
        .fillna("Unknown")
        .astype(str)
        .value_counts()
    )

    st.bar_chart(
        severity_chart
    )

    # -------------------------------
    # Most Affected Components
    # -------------------------------

    st.subheader("📈 Most Affected Components")

    component_chart_df = df[
        ~df["Component"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(
            [
                "unknown",
                "none",
                "n/a",
                "nan"
            ]
        )
    ]

    if len(component_chart_df) > 0:

        component_chart = (
            component_chart_df["Component"]
            .value_counts()
        )

        st.bar_chart(
            component_chart
        )

    else:

        st.info(
            "No identified component patterns available yet."
        )

    # -------------------------------
    # Most Common Root Causes
    # -------------------------------

    st.subheader("📈 Most Common Root Causes")

    root_cause_chart_df = df[
        ~df["Root Cause"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(
            [
                "unknown",
                "none",
                "n/a",
                "nan",
                "unable to determine the exact cause."
            ]
        )
    ]

    if len(root_cause_chart_df) > 0:

        root_cause_chart = (
            root_cause_chart_df["Root Cause"]
            .value_counts()
        )

        st.bar_chart(
            root_cause_chart
        )

    else:

        st.info(
            "No identified root-cause patterns available yet."
        )

    # ===============================
    # Recent Analyses
    # ===============================

    st.divider()

    st.subheader("📋 Recent Bug Analyses")

    st.dataframe(
        df,
        use_container_width=True
    )