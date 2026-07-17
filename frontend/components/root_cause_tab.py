import streamlit as st


def show_root_cause_tab(root_cause):

    st.subheader("🧠 Root Cause Analysis")

    st.error(root_cause["Root Cause"])

    st.subheader("📖 Technical Explanation")

    st.info(root_cause["Technical Explanation"])

    st.subheader("📦 Affected Module")

    st.success(root_cause["Affected Module"])