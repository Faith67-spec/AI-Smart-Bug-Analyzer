from io import BytesIO
from datetime import datetime
import uuid

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from reportlab.pdfbase.pdfmetrics import stringWidth

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    HRFlowable,
    KeepTogether
)

###############################################################################
#                            REPORT THEME
###############################################################################

PRIMARY = HexColor("#0F4C81")
SECONDARY = HexColor("#1F77B4")
ACCENT = HexColor("#D9EAF7")

LIGHT = HexColor("#F8F9FA")
DARK = HexColor("#202124")

SUCCESS = HexColor("#2E7D32")
WARNING = HexColor("#ED6C02")
DANGER = HexColor("#D32F2F")

BORDER = HexColor("#D0D7DE")

###############################################################################
#                              STYLES
###############################################################################

styles = getSampleStyleSheet()

TITLE = ParagraphStyle(

    "TITLE",

    parent=styles["Heading1"],

    alignment=TA_CENTER,

    fontName="Helvetica-Bold",

    fontSize=28,

    leading=34,

    textColor=PRIMARY,

    spaceAfter=6

)

SUBTITLE = ParagraphStyle(

    "SUBTITLE",

    parent=styles["Heading2"],

    alignment=TA_CENTER,

    fontName="Helvetica",

    fontSize=15,

    leading=18,

    textColor=colors.grey,

    spaceAfter=20

)

HEADING = ParagraphStyle(

    "HEADING",

    parent=styles["Heading2"],

    fontName="Helvetica-Bold",

    fontSize=17,

    leading=22,

    textColor=PRIMARY,

    spaceBefore=12,

    spaceAfter=10

)

BODY = ParagraphStyle(

    "BODY",

    parent=styles["BodyText"],

    fontName="Helvetica",

    fontSize=10,

    leading=16,

    textColor=DARK

)

SMALL = ParagraphStyle(

    "SMALL",

    parent=styles["BodyText"],

    fontSize=8,

    leading=11,

    textColor=colors.grey

)

CODE = ParagraphStyle(

    "CODE",

    parent=styles["Code"],

    fontName="Courier",

    fontSize=8,

    leading=10,

    backColor=LIGHT,

    borderPadding=6

)

###############################################################################
#                        REPORT HELPERS
###############################################################################

def report_id():

    return "BUG-" + datetime.now().strftime("%Y%m%d") + "-" + str(uuid.uuid4())[:8].upper()


def report_time():

    return datetime.now().strftime("%d %B %Y %H:%M:%S")


def horizontal_line():

    return HRFlowable(

        width="100%",

        thickness=1,

        color=BORDER,

        spaceBefore=6,

        spaceAfter=10

    )


def section_header(title):

    banner = Table(

        [[Paragraph(f"<b>{title}</b>", BODY)]],

        colWidths=[6.5 * inch]

    )

    banner.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,-1),PRIMARY),

            ("TEXTCOLOR",(0,0),(-1,-1),colors.white),

            ("BOTTOMPADDING",(0,0),(-1,-1),10),

            ("TOPPADDING",(0,0),(-1,-1),10),

            ("LEFTPADDING",(0,0),(-1,-1),10),

            ("RIGHTPADDING",(0,0),(-1,-1),10)

        ])

    )

    return banner


###############################################################################
#                  EXECUTIVE SUMMARY CARD
###############################################################################

def summary_card(title,value):

    card = Table(

        [

            [

                Paragraph(

                    f"<b>{title}</b>",

                    SMALL

                )

            ],

            [

                Paragraph(

                    str(value),

                    BODY

                )

            ]

        ],

        colWidths=[2.1*inch]

    )

    card.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),PRIMARY),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("BACKGROUND",(0,1),(-1,-1),LIGHT),

            ("BOX",(0,0),(-1,-1),1,BORDER),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8),

            ("ALIGN",(0,0),(-1,-1),"CENTER")

        ])

    )

    return card


###############################################################################
#                       FOOTER
###############################################################################

def footer(canvas,doc):

    canvas.saveState()

    canvas.setStrokeColor(BORDER)

    canvas.line(40,35,555,35)

    canvas.setFont("Helvetica",8)

    canvas.setFillColor(colors.grey)

    canvas.drawString(

        40,

        20,

        "TEST PDF VERSION 999| Intelligent Multi-Agent Software Defect Analysis"

    )

    canvas.drawRightString(

        555,

        20,

        f"Page {doc.page}"

    )

    canvas.restoreState()

    ###############################################################################
#                           COVER PAGE
###############################################################################

def add_cover_page(elements):

    report = report_id()

    generated = report_time()

    # =====================================================
    # Blue Banner
    # =====================================================

    banner = Table(

        [[Paragraph(
            "<font color='white'><b>AI SMART BUG ANALYZER</b></font>",
            TITLE
        )]],

        colWidths=[6.5*inch]

    )

    banner.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,-1),PRIMARY),

            ("BOTTOMPADDING",(0,0),(-1,-1),22),

            ("TOPPADDING",(0,0),(-1,-1),22),

            ("ALIGN",(0,0),(-1,-1),"CENTER")

        ])

    )

    elements.append(banner)

    elements.append(Spacer(1,0.30*inch))

    elements.append(

        Paragraph(

            "Intelligent Multi-Agent Software Defect Analysis Report",

            SUBTITLE

        )

    )

    elements.append(horizontal_line())

    ###########################################################################
    # Report Information
    ###########################################################################

    info = Table(

        [

            ["Report ID",report],

            ["Generated",generated],

            ["Prepared By","AI Smart Bug Analyzer"],

            ["Analysis Engine","Multi-Agent AI + RAG"],

            ["Knowledge Base","Eclipse Bugzilla Historical Defects"]

        ],

        colWidths=[2.0*inch,4.5*inch]

    )

    info.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(0,-1),ACCENT),

            ("TEXTCOLOR",(0,0),(-1,-1),DARK),

            ("GRID",(0,0),(-1,-1),0.5,BORDER),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8),

            ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold")

        ])

    )

    elements.append(info)

    elements.append(Spacer(1,0.40*inch))

    ###########################################################################
    # Executive Introduction
    ###########################################################################

    intro = """
This engineering report was automatically generated by the
<b>AI Smart Bug Analyzer</b>.

The platform analyses software defects using a collaborative
Multi-Agent Artificial Intelligence architecture.

Each submitted defect is independently analysed using:

• Intelligent Bug Triage

• Log Analysis

• Root Cause Analysis

• Duplicate Detection

• Retrieval-Augmented Generation (RAG)

• Historical Defect Retrieval

• Engineering Best Practice Recommendations

The resulting analysis is fully explainable and supported
by historical software defect knowledge whenever possible.
"""

    elements.append(

        Paragraph(

            intro,

            BODY

        )

    )

    elements.append(Spacer(1,0.35*inch))

    ###########################################################################
    # AI Capabilities
    ###########################################################################

    capability = Table(

        [

            ["AI Capability","Status"],

            ["Bug Triage","✓"],

            ["Log Analysis","✓"],

            ["Root Cause Analysis","✓"],

            ["Duplicate Detection","✓"],

            ["Semantic Search","✓"],

            ["RAG Retrieval","✓"],

            ["Engineering Recommendations","✓"]

        ],

        colWidths=[5.2*inch,1.0*inch]

    )

    capability.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),PRIMARY),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),0.5,BORDER),

            ("BACKGROUND",(0,1),(-1,-1),LIGHT),

            ("ALIGN",(1,1),(-1,-1),"CENTER"),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8)

        ])

    )

    elements.append(capability)

    elements.append(PageBreak())


###############################################################################
#                     EXECUTIVE SUMMARY
###############################################################################

def add_executive_summary(

    elements,

    triage,

    root_cause

):

    elements.append(

        section_header(

            "EXECUTIVE SUMMARY"

        )

    )

    elements.append(

        Spacer(1,0.18*inch)

    )

    row1 = [

        summary_card(

            "Severity",

            triage["Severity"]

        ),

        summary_card(

            "Priority",

            triage["Priority"]

        ),

        summary_card(

            "Confidence",

            f'{root_cause["Confidence"]}%'

        )

    ]

    row2 = [

        summary_card(

            "Component",

            triage["Component"]

        ),

        summary_card(

            "Module",

            root_cause["Affected Module"]

        ),

        summary_card(

            "Analysis",

            "AI + RAG"

            if root_cause["Supporting Evidence"]

            else

            "AI"

        )

    ]

    elements.append(

        Table(

            [row1,row2],

            colWidths=[2.15*inch]*3

        )

    )

    elements.append(

        Spacer(1,0.30*inch)

    )

    elements.append(

        Paragraph(

"""
The submitted software defect has been analysed using a
multi-agent AI pipeline. The analysis includes intelligent
triage, stack trace inspection, root cause reasoning,
semantic similarity retrieval and engineering
recommendation generation.

The following sections provide a detailed explanation of
the identified defect together with supporting historical
evidence and recommended remediation actions.
""",

            BODY

        )

    )

    elements.append(

        Spacer(1,0.35*inch)

    )
    ###############################################################################
#                         BUG REPORT
###############################################################################

def add_bug_report(
    elements,
    bug_report
):

    elements.append(
        section_header(
            "SUBMITTED BUG REPORT"
        )
    )

    elements.append(
        Spacer(1,0.15*inch)
    )

    if not bug_report.strip():

        bug_report = "No bug description was provided."

    bug_box = Table(

        [[Paragraph(
            bug_report.replace("\n","<br/>"),
            BODY
        )]],

        colWidths=[6.5*inch]

    )

    bug_box.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,-1),LIGHT),

            ("BOX",(0,0),(-1,-1),1,BORDER),

            ("LEFTPADDING",(0,0),(-1,-1),12),

            ("RIGHTPADDING",(0,0),(-1,-1),12),

            ("TOPPADDING",(0,0),(-1,-1),12),

            ("BOTTOMPADDING",(0,0),(-1,-1),12)

        ])

    )

    elements.append(bug_box)

    elements.append(Spacer(1,0.30*inch))


###############################################################################
#                         STACK TRACE
###############################################################################

def add_stack_trace(
    elements,
    uploaded_log
):

    elements.append(
        section_header(
            "STACK TRACE / ERROR LOG"
        )
    )

    elements.append(
        Spacer(1,0.15*inch)
    )

    if not uploaded_log.strip():

        uploaded_log = "No log file was supplied."

    uploaded_log = uploaded_log.replace("&","&amp;")
    uploaded_log = uploaded_log.replace("<","&lt;")
    uploaded_log = uploaded_log.replace(">","&gt;")
    uploaded_log = uploaded_log.replace("\n","<br/>")

    stack = Table(

        [[Paragraph(
            uploaded_log,
            CODE
        )]],

        colWidths=[6.5*inch]

    )

    stack.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,-1),HexColor("#F3F5F7")),

            ("BOX",(0,0),(-1,-1),1,BORDER),

            ("LEFTPADDING",(0,0),(-1,-1),10),

            ("RIGHTPADDING",(0,0),(-1,-1),10),

            ("TOPPADDING",(0,0),(-1,-1),10),

            ("BOTTOMPADDING",(0,0),(-1,-1),10)

        ])

    )

    elements.append(stack)

    elements.append(Spacer(1,0.30*inch))


###############################################################################
#                     AI TRIAGE RESULTS
###############################################################################

def add_triage(
    elements,
    triage
):

    elements.append(
        section_header(
            "AI BUG TRIAGE"
        )
    )

    elements.append(
        Spacer(1,0.15*inch)
    )

    triage_table = Table(

        [

            ["Attribute","Result"],

            ["Severity",triage["Severity"]],

            ["Priority",triage["Priority"]],

            ["Component",triage["Component"]],

            ["Confidence",f'{triage["Confidence"]}%']

        ],

        colWidths=[2.3*inch,4.2*inch]

    )

    triage_table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),PRIMARY),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("BACKGROUND",(0,1),(0,-1),ACCENT),

            ("GRID",(0,0),(-1,-1),0.5,BORDER),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("FONTNAME",(0,1),(0,-1),"Helvetica-Bold")

        ])

    )

    elements.append(triage_table)

    elements.append(Spacer(1,0.30*inch))


###############################################################################
#                     LOG ANALYSIS
###############################################################################

def add_log_analysis(
    elements,
    log_analysis
):

    elements.append(
        section_header(
            "LOG ANALYSIS"
        )
    )

    elements.append(
        Spacer(1,0.15*inch)
    )

    table = Table(

        [

            ["Analysis","Finding"],

            ["Exception Type",
             log_analysis["Exception Type"]],

            ["Failure Point",
             log_analysis["Failure Point"]],

            ["Likely Cause",
             log_analysis["Likely Cause"]]

        ],

        colWidths=[2.3*inch,4.2*inch]

    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),PRIMARY),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("BACKGROUND",(0,1),(0,-1),ACCENT),

            ("GRID",(0,0),(-1,-1),0.5,BORDER),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("FONTNAME",(0,1),(0,-1),"Helvetica-Bold")

        ])

    )

    elements.append(table)

    elements.append(Spacer(1,0.20*inch))

    note = Table(

        [[Paragraph("""

<b>AI Log Analysis Summary</b><br/><br/>

The uploaded log was automatically inspected by the Log Analysis
Agent. Exception patterns, stack trace locations and probable
failure points were extracted before being forwarded to the
Root Cause Agent for deeper reasoning.

""",BODY)]],

        colWidths=[6.5*inch]

    )

    note.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,-1),HexColor("#EEF6FC")),

            ("BOX",(0,0),(-1,-1),1,SECONDARY),

            ("LEFTPADDING",(0,0),(-1,-1),12),

            ("RIGHTPADDING",(0,0),(-1,-1),12),

            ("TOPPADDING",(0,0),(-1,-1),10),

            ("BOTTOMPADDING",(0,0),(-1,-1),10)

        ])

    )

    elements.append(note)

    elements.append(Spacer(1,0.35*inch))
    ###############################################################################
#                    ROOT CAUSE ANALYSIS
###############################################################################

def add_root_cause_analysis(
    elements,
    root_cause
):

    elements.append(
        section_header(
            "ROOT CAUSE ANALYSIS"
        )
    )

    elements.append(
        Spacer(1,0.15*inch)
    )

    source = (
        "Historical Evidence + AI Reasoning"
        if root_cause["Supporting Evidence"]
        else
        "AI Reasoning"
    )

    investigation = Table(

        [

            ["Investigation","Result"],

            ["Root Cause",
             root_cause["Root Cause"]],

            ["Confidence",
             f'{root_cause["Confidence"]}%'],

            ["Affected Module",
             root_cause["Affected Module"]],

            ["Analysis Source",
             source]

        ],

        colWidths=[2.3*inch,4.2*inch]

    )

    investigation.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),PRIMARY),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("BACKGROUND",(0,1),(0,-1),ACCENT),

            ("GRID",(0,0),(-1,-1),0.5,BORDER),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("FONTNAME",(0,1),(0,-1),"Helvetica-Bold")

        ])

    )

    elements.append(investigation)

    elements.append(
        Spacer(1,0.20*inch)
    )

    explanation = Table(

        [[

            Paragraph(

                f"""

<b>Technical Explanation</b>

<br/><br/>

{root_cause["Technical Explanation"]}

""",

                BODY

            )

        ]],

        colWidths=[6.5*inch]

    )

    explanation.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,-1),LIGHT),

            ("BOX",(0,0),(-1,-1),1,BORDER),

            ("LEFTPADDING",(0,0),(-1,-1),12),

            ("RIGHTPADDING",(0,0),(-1,-1),12),

            ("TOPPADDING",(0,0),(-1,-1),10),

            ("BOTTOMPADDING",(0,0),(-1,-1),10)

        ])

    )

    elements.append(explanation)

    elements.append(
        Spacer(1,0.30*inch)
    )

###############################################################################
#                  SUPPORTING HISTORICAL EVIDENCE
###############################################################################

def add_historical_evidence(
    elements,
    root_cause
):

    evidence = root_cause.get(
        "Supporting Evidence"
    )

    if not evidence:
        return

    elements.append(

        section_header(

            "SUPPORTING HISTORICAL EVIDENCE"

        )

    )

    elements.append(
        Spacer(1,0.15*inch)
    )

    table = Table(

        [

            ["Evidence","Value"],

            ["Similarity",
             f'{evidence["Similarity"]:.2f}%'],

            ["Knowledge Base",
             "Eclipse Bugzilla"],

            ["Retrieval Method",
             "Semantic Similarity Search (RAG)"]

        ],

        colWidths=[2.3*inch,4.2*inch]

    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),PRIMARY),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("BACKGROUND",(0,1),(0,-1),ACCENT),

            ("GRID",(0,0),(-1,-1),0.5,BORDER),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8)

        ])

    )

    elements.append(table)

    elements.append(
        Spacer(1,0.15*inch)
    )

    bug = Table(

        [[

            Paragraph(

                evidence["Historical Bug"].replace(
                    "\n",
                    "<br/>"
                ),

                BODY

            )

        ]],

        colWidths=[6.5*inch]

    )

    bug.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,-1),HexColor("#F9FBFC")),

            ("BOX",(0,0),(-1,-1),1,BORDER),

            ("LEFTPADDING",(0,0),(-1,-1),12),

            ("RIGHTPADDING",(0,0),(-1,-1),12),

            ("TOPPADDING",(0,0),(-1,-1),10),

            ("BOTTOMPADDING",(0,0),(-1,-1),10)

        ])

    )

    elements.append(bug)

    elements.append(
        Spacer(1,0.30*inch)
    )

###############################################################################
#                 SIMILAR HISTORICAL BUGS
###############################################################################

def add_similar_bugs(
    elements,
    similar_bugs
):

    elements.append(
        section_header(
            "SIMILAR HISTORICAL BUGS"
        )
    )

    elements.append(
        Spacer(1,0.15*inch)
    )

    if len(similar_bugs) == 0:

        elements.append(

            Paragraph(

                "No sufficiently similar historical defects were retrieved.",

                BODY

            )

        )

        elements.append(
            Spacer(1,0.20*inch)
        )

        return

    for i, bug in enumerate(
        similar_bugs,
        start=1
    ):

        meta = bug["Metadata"]

        summary = Table(

            [

                ["Historical Bug",
                 f"#{i}"],

                ["Similarity",
                 f'{bug["Similarity"]:.2f}%'],

                ["Bug ID",
                 meta.get("Bug_ID","Unknown")],

                ["Product",
                 meta.get("Product","Unknown")],

                ["Component",
                 meta.get("Component","Unknown")]

            ],

            colWidths=[2.2*inch,4.3*inch]

        )

        summary.setStyle(

            TableStyle([

                ("BACKGROUND",(0,0),(0,-1),ACCENT),

                ("GRID",(0,0),(-1,-1),0.5,BORDER),

                ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),

                ("BOTTOMPADDING",(0,0),(-1,-1),8),

                ("TOPPADDING",(0,0),(-1,-1),8)

            ])

        )

        elements.append(summary)

        elements.append(
            Spacer(1,0.10*inch)
        )

        details = Table(

            [[

                Paragraph(

                    bug["Bug"].replace(
                        "\n",
                        "<br/>"
                    ),

                    BODY

                )

            ]],

            colWidths=[6.5*inch]

        )

        details.setStyle(

            TableStyle([

                ("BACKGROUND",(0,0),(-1,-1),LIGHT),

                ("BOX",(0,0),(-1,-1),1,BORDER),

                ("LEFTPADDING",(0,0),(-1,-1),10),

                ("RIGHTPADDING",(0,0),(-1,-1),10),

                ("TOPPADDING",(0,0),(-1,-1),8),

                ("BOTTOMPADDING",(0,0),(-1,-1),8)

            ])

        )

        elements.append(details)

        elements.append(
            Spacer(1,0.25*inch)
        )

        ###############################################################################
#                    REMEDIATION RECOMMENDATIONS
###############################################################################

def add_recommendations(
    elements,
    recommendations
):

    elements.append(
        section_header(
            "REMEDIATION RECOMMENDATIONS"
        )
    )

    elements.append(
        Spacer(1, 0.15 * inch)
    )

    if not recommendations:

        elements.append(
            Paragraph(
                "No recommendations were generated.",
                BODY
            )
        )

        elements.append(
            Spacer(1,0.25*inch)
        )

        return

    for i, recommendation in enumerate(recommendations, start=1):

        card = Table(

            [[

                Paragraph(

                    f"<b>Recommendation {i}</b><br/><br/>{recommendation}",

                    BODY

                )

            ]],

            colWidths=[6.5*inch]

        )

        card.setStyle(

            TableStyle([

                ("BACKGROUND",(0,0),(-1,-1),HexColor("#F8FFF4")),

                ("BOX",(0,0),(-1,-1),1,SUCCESS),

                ("LEFTPADDING",(0,0),(-1,-1),12),

                ("RIGHTPADDING",(0,0),(-1,-1),12),

                ("TOPPADDING",(0,0),(-1,-1),10),

                ("BOTTOMPADDING",(0,0),(-1,-1),10)

            ])

        )

        elements.append(card)

        elements.append(
            Spacer(1,0.12*inch)
        )


###############################################################################
#                         AI METHODOLOGY
###############################################################################

def add_ai_methodology(
    elements
):

    elements.append(PageBreak())

    elements.append(
        section_header(
            "AI METHODOLOGY"
        )
    )

    elements.append(
        Spacer(1,0.20*inch)
    )

    methodology = """

<b>AI Smart Bug Analyzer</b> uses a Multi-Agent Artificial
Intelligence architecture for automated software defect analysis.

The complete analysis pipeline consists of:

• Bug Triage Agent

• Log Analysis Agent

• Root Cause Agent

• Recommendation Agent

• Duplicate Detection Agent

• Semantic Similarity Search

• Retrieval-Augmented Generation (RAG)

• Eclipse Bugzilla Knowledge Base

Each submitted defect is analysed independently before the
results are combined into a unified engineering report.

Historical defects retrieved through semantic similarity
search are used as supporting evidence to improve confidence,
explainability and recommendation quality.

"""

    elements.append(
        Paragraph(
            methodology,
            BODY
        )
    )

    elements.append(
        Spacer(1,0.30*inch)
    )

    info = Table(

        [

            ["Analysis Engine","Multi-Agent AI"],

            ["Embedding Model","all-MiniLM-L6-v2"],

            ["Vector Database","ChromaDB"],

            ["Knowledge Source","Eclipse Bugzilla"],

            ["Reasoning","Rule-Based + RAG"],

            ["Generated",report_time()]

        ],

        colWidths=[2.4*inch,4.1*inch]

    )

    info.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(0,-1),ACCENT),

            ("GRID",(0,0),(-1,-1),0.5,BORDER),

            ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8)

        ])

    )

    elements.append(info)

    elements.append(
        Spacer(1,0.40*inch)
    )

    elements.append(
        Paragraph(
            "<b>End of Report</b>",
            HEADING
        )
    )

    elements.append(
        Paragraph(
            """
This report was automatically generated by the AI Smart Bug
Analyzer platform. The results are intended to assist software
engineers by providing explainable AI-assisted defect analysis,
historical evidence and remediation recommendations.

© AI Smart Bug Analyzer
""",
            BODY
        )
    )


###############################################################################
#                    MAIN PDF GENERATOR
###############################################################################

def generate_pdf_report(

    bug_report,
    uploaded_log,
    triage,
    log_analysis,
    root_cause,
    similar_bugs,
    recommendations

):

    buffer = BytesIO()

    doc = SimpleDocTemplate(

        buffer,

        pagesize=A4,

        rightMargin=40,

        leftMargin=40,

        topMargin=45,

        bottomMargin=45

    )

    elements = []

    ###########################################################################
    # Cover Page
    ###########################################################################

    add_cover_page(
        elements
    )

    ###########################################################################
    # Executive Summary
    ###########################################################################

    add_executive_summary(
        elements,
        triage,
        root_cause
    )

    ###########################################################################
    # Bug Report
    ###########################################################################

    add_bug_report(
        elements,
        bug_report
    )

    ###########################################################################
    # Stack Trace
    ###########################################################################

    add_stack_trace(
        elements,
        uploaded_log
    )

    ###########################################################################
    # AI Triage
    ###########################################################################

    add_triage(
        elements,
        triage
    )

    ###########################################################################
    # Log Analysis
    ###########################################################################

    add_log_analysis(
        elements,
        log_analysis
    )

    ###########################################################################
    # Root Cause
    ###########################################################################

    add_root_cause_analysis(
        elements,
        root_cause
    )

    ###########################################################################
    # Historical Evidence
    ###########################################################################

    add_historical_evidence(
        elements,
        root_cause
    )

    ###########################################################################
    # Similar Bugs
    ###########################################################################

    add_similar_bugs(
        elements,
        similar_bugs
    )

    ###########################################################################
    # Recommendations
    ###########################################################################

    add_recommendations(
        elements,
        recommendations
    )

    ###########################################################################
    # AI Methodology
    ###########################################################################

    add_ai_methodology(
        elements
    )

    ###########################################################################
    # Build PDF
    ###########################################################################

    doc.build(

        elements,

        onFirstPage=footer,

        onLaterPages=footer

    )

    pdf = buffer.getvalue()

    buffer.close()

    return pdf

