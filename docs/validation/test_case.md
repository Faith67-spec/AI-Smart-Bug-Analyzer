# Milestone 2 Test Cases

## AI Smart Bug Analyzer & AI Fixer

### Infosys Springboard Virtual Internship 7.0

---

# Objective

This document contains the complete set of validation test cases used to evaluate the **Triage Agent** and **Log Analysis Agent** implemented in the AI Smart Bug Analyzer.

The test cases cover a wide variety of bug report formats and software error types using the seeded historical defect dataset, ensuring that the implemented agents correctly classify bug severity, determine affected components, and extract useful diagnostic information from uploaded logs.

---

# Validation Scope

The following functionality was validated:

- Triage Agent
  - Severity Classification
  - Priority Assignment
  - Component Detection
  - Confidence Score
  - AI Reasoning

- Log Analysis Agent
  - Exception Detection
  - Failure Point Extraction
  - Affected Code Path Extraction
  - Root Cause Identification

---

# TC-01 Login Failure

## Category

Authentication

## Bug Report

Users are unable to log in after resetting their password.

The password reset process completes successfully, but when users attempt to log in with the new password, the application displays **"Invalid Credentials"**.

## Log File

login_failure.log

## Expected Result

**Triage Agent**

- Severity: High
- Priority: P2
- Component: Authentication

**Log Analysis Agent**

- Detect authentication-related failure
- Extract exception (if available)
- Identify failure point from stack trace
- Display affected code path

---

# TC-02 Database Connection Failure

## Category

Database

## Bug Report

The application fails to connect to the database during startup.

Users cannot access any functionality because the backend is unable to establish a database connection.

## Log File

database_connection.log

## Expected Result

**Triage Agent**

- Severity: High
- Priority: P2
- Component: Database

**Log Analysis Agent**

- Detect CannotGetJdbcConnectionException
- Identify database connection failure
- Extract failure point
- Display affected code path

---

# TC-03 NullPointerException

## Category

Runtime Exception

## Bug Report

The application crashes immediately after clicking the Login button.

## Log File

null_pointer.log

## Expected Result

**Triage Agent**

- Severity: Critical
- Priority: P1
- Component: Backend

**Log Analysis Agent**

- Detect NullPointerException
- Extract controller method
- Identify affected code path
- Suggest likely cause

---

# TC-04 File Not Found

## Category

File System

## Bug Report

The application fails while loading the configuration file during startup.

## Log File

file_not_found.log

## Expected Result

**Triage Agent**

- Severity: Medium
- Priority: P3
- Component: File System

**Log Analysis Agent**

- Detect FileNotFoundException
- Identify missing resource
- Display affected code path

---

# TC-05 OutOfMemoryError

## Category

Memory Management

## Bug Report

The application becomes extremely slow before crashing with an out-of-memory error while processing a large dataset.

## Log File

out_of_memory.log

## Expected Result

**Triage Agent**

- Severity: Critical
- Priority: P1
- Component: Memory

**Log Analysis Agent**

- Detect OutOfMemoryError
- Identify affected module
- Suggest memory exhaustion as likely cause

---

# TC-06 API Timeout

## Category

API

## Bug Report

The payment service fails because the external API does not respond within the configured timeout period.

## Log File

api_timeout.log

## Expected Result

**Triage Agent**

- Severity: Medium
- Priority: P3
- Component: API

**Log Analysis Agent**

- Detect timeout exception
- Identify API call
- Display affected code path

---

# TC-07 Permission Denied

## Category

Security

## Bug Report

Users receive an access denied message when attempting to generate administrative reports.

## Log File

permission_denied.log

## Expected Result

**Triage Agent**

- Severity: Medium
- Priority: P3
- Component: Security

**Log Analysis Agent**

- Detect AccessDeniedException
- Identify restricted operation
- Display affected code path

---

# TC-08 Network Error

## Category

Network

## Bug Report

The application cannot communicate with the remote service due to a network connectivity issue.

## Log File

network_error.log

## Expected Result

**Triage Agent**

- Severity: High
- Priority: P2
- Component: Network

**Log Analysis Agent**

- Detect ConnectException
- Identify connection failure
- Display affected code path

---

# TC-09 UI Rendering Issue

## Category

User Interface

## Bug Report

The dashboard loads successfully, but charts and widgets fail to render correctly after logging in.

## Log File

ui_render.log

## Expected Result

**Triage Agent**

- Severity: Low
- Priority: P4
- Component: User Interface

**Log Analysis Agent**

- Identify frontend rendering issue
- Report absence of stack trace if none exists

---

# TC-10 SQL Syntax Error

## Category

Database

## Bug Report

Generating the monthly sales report fails due to an invalid SQL query.

## Log File

sql_syntax.log

## Expected Result

**Triage Agent**

- Severity: Medium
- Priority: P3
- Component: Database

**Log Analysis Agent**

- Detect SQLSyntaxErrorException
- Identify SQL execution failure
- Display affected code path

---

# TC-11 HTTP 500 Internal Server Error

## Category

Web Server

## Bug Report

Users receive an HTTP 500 Internal Server Error while submitting the registration form.

## Log File

http500.log

## Expected Result

**Triage Agent**

- Severity: High
- Priority: P2
- Component: Web Server

**Log Analysis Agent**

- Detect Internal Server Error
- Identify server-side failure
- Display affected code path

---

# TC-12 IndexOutOfBoundsException

## Category

Runtime Exception

## Bug Report

The application crashes while generating reports containing more than 500 records.

## Log File

index_out_of_bounds.log

## Expected Result

**Triage Agent**

- Severity: Medium
- Priority: P3
- Component: Backend

**Log Analysis Agent**

- Detect IndexOutOfBoundsException
- Extract failure point
- Display affected code path
- Suggest array/list boundary issue

---

# Test Coverage Summary

| Test Case | Category | Bug Format | Uploaded Log |
|------------|----------|------------|--------------|
| TC-01 | Login Failure | Plain Text | login_failure.log |
| TC-02 | Database Connection | Plain Text | database_connection.log |
| TC-03 | NullPointerException | Plain Text | null_pointer.log |
| TC-04 | File Not Found | Plain Text | file_not_found.log |
| TC-05 | OutOfMemoryError | Plain Text | out_of_memory.log |
| TC-06 | API Timeout | Plain Text | api_timeout.log |
| TC-07 | Permission Denied | Plain Text | permission_denied.log |
| TC-08 | Network Error | Plain Text | network_error.log |
| TC-09 | UI Rendering | Plain Text | ui_render.log |
| TC-10 | SQL Syntax Error | Plain Text | sql_syntax.log |
| TC-11 | HTTP 500 | Plain Text | http500.log |
| TC-12 | IndexOutOfBoundsException | Plain Text | index_out_of_bounds.log |

---

# Expected Validation Outcome

Successful completion of these test cases demonstrates that:

- The Triage Agent accurately classifies bug severity and priority.
- The Triage Agent correctly identifies affected software components.
- The Log Analysis Agent successfully extracts exception types from uploaded logs.
- Failure points and affected code paths are correctly identified from stack traces.
- AI reasoning and likely causes are generated appropriately.
- The multi-agent orchestration successfully processes diverse bug report formats and software error types using the seeded historical defect dataset.

This test suite satisfies the Milestone 2 validation requirement:

> **Validate Triage and Log Analysis agent accuracy across varied bug report formats and error types using seeded dataset.**