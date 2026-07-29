import io

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)


def generate_pdf_report(
    bug_report,
    log,
    triage,
    log_analysis,
    root_cause,
    similar_bugs,
    recommendations
):

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    # -------------------------------------------------
    # Title
    # -------------------------------------------------

    story.append(
        Paragraph(
            "AI Smart Bug Analyzer & Fix Advisor",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            "Bug Analysis Report",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 20))

    # -------------------------------------------------
    # Bug Description
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Submitted Bug</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            bug_report.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 15))

    # -------------------------------------------------
    # Uploaded Log
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Uploaded Log</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            log.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 15))

    # -------------------------------------------------
    # Triage
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Triage Analysis</b>",
            styles["Heading2"]
        )
    )

    for key, value in triage.items():

        story.append(
            Paragraph(
                f"<b>{key}</b>: {value}",
                styles["BodyText"]
            )
        )

    story.append(Spacer(1, 15))

    # -------------------------------------------------
    # Log Analysis
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Log Analysis</b>",
            styles["Heading2"]
        )
    )

    for key, value in log_analysis.items():

        story.append(
            Paragraph(
                f"<b>{key}</b>: {value}",
                styles["BodyText"]
            )
        )

    story.append(Spacer(1, 15))

    # -------------------------------------------------
    # Root Cause
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Root Cause Analysis</b>",
            styles["Heading2"]
        )
    )

    for key, value in root_cause.items():

        if key != "Supporting Evidence":

            story.append(
                Paragraph(
                    f"<b>{key}</b>: {value}",
                    styles["BodyText"]
                )
            )

    story.append(Spacer(1, 15))

    # -------------------------------------------------
    # Similar Bugs
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Similar Historical Bugs</b>",
            styles["Heading2"]
        )
    )

    for bug in similar_bugs:

        story.append(
            Paragraph(
                f"Similarity: {round(bug['Similarity'])}%",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                bug["Bug"],
                styles["BodyText"]
            )
        )

        story.append(Spacer(1, 10))

    # -------------------------------------------------
    # Recommendations
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Recommendations</b>",
            styles["Heading2"]
        )
    )

    for rec in recommendations:

        story.append(
            Paragraph(
                f"• {rec}",
                styles["BodyText"]
            )
        )

    doc.build(story)

    buffer.seek(0)

    return buffer