import re
import streamlit as st


def get_badge(similarity):

    if similarity >= 90:
        return "🟢 Nearly Identical Match"

    elif similarity >= 80:
        return "🟢 Strong Semantic Match"

    elif similarity >= 70:
        return "🟡 Good Semantic Match"

    elif similarity >= 60:
        return "🟠 Moderate Semantic Match"

    elif similarity >= 50:
        return "🟠 Related Historical Match"

    return "⚪ Low Semantic Similarity"


def extract(pattern, text):

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group(1).strip()

    return "Unknown"


def parse_bug(text):

    return {

        "Product": extract(
            r"Product:\s*(.*?)\s*Component:",
            text
        ),

        "Component": extract(
            r"Component:\s*(.*?)\s*Severity:",
            text
        ),

        "Severity": extract(
            r"Severity:\s*(.*?)\s*Priority:",
            text
        ),

        "Priority": extract(
            r"Priority:\s*(.*?)\s*Summary:",
            text
        ),

        "Summary": extract(
            r"Summary:\s*(.*?)\s*Resolution:",
            text
        ),

        "Resolution": extract(
            r"Resolution:\s*(.*)",
            text
        )

    }


def show_similar_bug_tab(similar_bugs):

    st.subheader("📚 Top Retrieved Historical Matches (RAG)")

    st.caption(
        "Semantic retrieval performed over the Eclipse Bugzilla historical defect knowledge base."
    )

    if len(similar_bugs) == 0:

        st.info(
            """
### No Historical Defects Retrieved

No relevant historical defects were retrieved from the knowledge base.

The Root Cause Analysis and Remediation Recommendations
were therefore generated primarily using AI reasoning and
software engineering best practices.
"""
        )

        return

    for i, bug in enumerate(similar_bugs, start=1):

        similarity = bug["Similarity"]

        metadata = bug["Metadata"]

        parsed = parse_bug(
            bug["Bug"]
        )

        st.divider()

        st.markdown(f"## 🐞 Retrieved Match #{i}")

        col1, col2 = st.columns([3, 1])

        with col1:

            badge = get_badge(similarity)

            if similarity >= 80:

                st.success(badge)

            elif similarity >= 60:

                st.warning(badge)

            else:

                st.info(badge)

        with col2:

            st.metric(
                "Semantic Similarity",
                f"{similarity:.2f}%"
            )

        st.progress(similarity / 100)

        st.subheader("📦 Historical Defect Details")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Product",
                parsed["Product"]
            )

            st.metric(
                "Severity",
                parsed["Severity"]
            )

        with c2:

            st.metric(
                "Component",
                parsed["Component"]
            )

            st.metric(
                "Priority",
                parsed["Priority"]
            )

        with c3:

            st.metric(
                "Bug ID",
                metadata.get(
                    "Bug_ID",
                    "Unknown"
                )
            )

            st.metric(
                "Resolution",
                parsed["Resolution"]
            )

        st.subheader("📝 Historical Resolution Summary")

        st.info(
            parsed["Summary"]
        )

        st.subheader("✅ Resolution Status")

        st.success(
            parsed["Resolution"]
        )

        st.subheader("📖 Retrieval Evidence")

        st.caption(
            f"""
Retrieved using Retrieval-Augmented Generation (RAG)
through semantic vector search over the Eclipse Bugzilla
knowledge base.

Similarity Score: **{similarity:.2f}%**
"""
        )