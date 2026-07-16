import streamlit as st


def show_recommendation_tab(triage, log):

    st.subheader("💡 AI Recommendations")

    exception = log["Exception Type"].lower()

    recommendations = []

    if "nullpointer" in exception:

        recommendations = [

            "Initialize objects before using them.",

            "Add null checks.",

            "Validate request input.",

            "Review authentication logic.",

            "Create unit tests."

        ]

    elif "jdbc" in exception or "connection" in exception:

        recommendations = [

            "Verify database server status.",

            "Check JDBC URL.",

            "Validate database credentials.",

            "Inspect firewall settings.",

            "Test database connectivity."

        ]

    else:

        recommendations = [

            "Review stack trace.",

            "Inspect recent code changes.",

            "Improve exception handling.",

            "Increase logging.",

            "Write regression tests."

        ]

    for item in recommendations:

        st.success(item)