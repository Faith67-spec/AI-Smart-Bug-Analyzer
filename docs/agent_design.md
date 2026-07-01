# Agent Responsibilities

## Triage Agent

Purpose:
Classify incoming defects.

Responsibilities:

- determine severity
- determine priority
- identify module
- classify defect type

Output:

Severity: High

Priority: P1

Module: Authentication

---

## Log Analysis Agent

Purpose:
Analyze stack traces.

Responsibilities:

- extract exceptions
- identify crash patterns
- detect error signatures

Output:

Exception:
NullPointerException

File:
UserController.java

Line:
42

---

## Duplicate Detection Agent

Purpose:
Identify similar defects.

Responsibilities:

- semantic similarity search
- retrieve top matches
- calculate similarity score

---

## Root Cause Agent

Purpose:
Predict probable cause.

Examples:

- null reference
- timeout
- configuration issue
- dependency conflict

---

## Remediation Agent

Purpose:
Recommend solutions.

Responsibilities:

- suggest fixes
- retrieve previous resolutions
- provide recommendations