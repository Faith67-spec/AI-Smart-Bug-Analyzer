import streamlit as st


def show_recommendation_tab(recommendations):

    st.subheader("💡 AI Recommendations")

    for item in recommendations:

        st.success(item)