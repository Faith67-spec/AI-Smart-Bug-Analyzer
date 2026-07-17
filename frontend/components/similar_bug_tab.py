import re
import streamlit as st


def get_badge(similarity):

    if similarity >= 90:
        return "🟢 Excellent Match"

    elif similarity >= 70:
        return "🟡 Strong Match"

    elif similarity >= 50:
        return "🟠 Moderate Match"

    return "🔴 Weak Match"


def extract(pattern, text):

    match = re.search(
        pattern,
        text,
        re.IGNORECASE
    )

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

    st.subheader("📚 Similar Historical Bugs")

    if len(similar_bugs) == 0:

        st.warning(
            "No similar historical bugs found."
        )

        return

    for i, bug in enumerate(similar_bugs, start=1):

        similarity = bug["Similarity"]

        metadata = bug["Metadata"]

        parsed = parse_bug(
            bug["Bug"]
        )

        st.divider()

        st.markdown(
            f"# 🐞 Historical Bug #{i}"
        )

        col1, col2 = st.columns([3,1])

        with col1:

            st.success(
                get_badge(similarity)
            )

        with col2:

            st.metric(
                "Similarity",
                f"{similarity}%"
            )

        st.progress(
            similarity / 100
        )

        st.subheader("📦 Bug Details")

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
                "Status",
                parsed["Resolution"]
            )

        st.subheader("📝 Summary")

        st.info(
            parsed["Summary"]
        )