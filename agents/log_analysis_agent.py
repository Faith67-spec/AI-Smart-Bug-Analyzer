import re


class LogAnalysisAgent:

    def __init__(self):

        self.rules = [

            {
                "keywords": [
                    "nullpointerexception"
                ],
                "exception": "NullPointerException",
                "failure": "Object Reference",
                "cause": "A null object reference was accessed before initialization.",
                "confidence": 98
            },

            {
                "keywords": [
                    "cannotgetjdbcconnectionexception",
                    "database connection"
                ],
                "exception": "CannotGetJdbcConnectionException",
                "failure": "Database Connection",
                "cause": "The application could not establish a database connection.",
                "confidence": 96
            },

            {
                "keywords": [
                    "sqlexception"
                ],
                "exception": "SQLException",
                "failure": "Database Query",
                "cause": "A database operation failed while executing an SQL statement.",
                "confidence": 95
            },

            {
                "keywords": [
                    "sqlsyntaxerrorexception",
                    "sql syntax"
                ],
                "exception": "SQLSyntaxErrorException",
                "failure": "Database Query",
                "cause": "The SQL query contains invalid syntax.",
                "confidence": 93
            },

            {
                "keywords": [
                    "indexoutofboundsexception"
                ],
                "exception": "IndexOutOfBoundsException",
                "failure": "Collection Access",
                "cause": "An invalid array or list index was accessed.",
                "confidence": 92
            },

            {
                "keywords": [
                    "outofmemoryerror",
                    "memory leak"
                ],
                "exception": "OutOfMemoryError",
                "failure": "Memory Allocation",
                "cause": "The JVM exhausted available heap memory.",
                "confidence": 98
            },

            {
                "keywords": [
                    "filenotfoundexception",
                    "file not found"
                ],
                "exception": "FileNotFoundException",
                "failure": "File Access",
                "cause": "The requested file could not be located.",
                "confidence": 90
            },

            {
                "keywords": [
                    "ioexception"
                ],
                "exception": "IOException",
                "failure": "Input / Output",
                "cause": "An input/output operation failed.",
                "confidence": 90
            },

            {
                "keywords": [
                    "connectexception",
                    "connection refused"
                ],
                "exception": "ConnectException",
                "failure": "Network Connection",
                "cause": "The application failed to connect to the remote server.",
                "confidence": 92
            },

            {
                "keywords": [
                    "timeout",
                    "timeoutexception"
                ],
                "exception": "TimeoutException",
                "failure": "API Request",
                "cause": "The request exceeded the configured timeout period.",
                "confidence": 89
            },

            {
                "keywords": [
                    "accessdeniedexception",
                    "permission denied",
                    "unauthorized"
                ],
                "exception": "AccessDeniedException",
                "failure": "Authorization",
                "cause": "The current user lacks sufficient permissions.",
                "confidence": 91
            },

            {
                "keywords": [
                    "http 500",
                    "internal server error"
                ],
                "exception": "HTTP 500",
                "failure": "Web Server",
                "cause": "The server encountered an unexpected internal error.",
                "confidence": 90
            },

            {
                "keywords": [
                    "invalid credentials",
                    "login",
                    "authentication",
                    "password reset"
                ],
                "exception": "Authentication Failure",
                "failure": "Login Module",
                "cause": "User authentication failed. The supplied credentials were rejected.",
                "confidence": 90
            },

            {
                "keywords": [
                    "payment",
                    "transaction failed"
                ],
                "exception": "Payment Processing Error",
                "failure": "Payment Gateway",
                "cause": "The payment request could not be completed.",
                "confidence": 91
            }

        ]

    def analyze(self, log):

        result = {

            "Exception Type": "Unknown",

            "Failure Point": "Unknown",

            "Affected Code Path": [],

            "Likely Cause": "Unable to determine.",

            "Confidence": 60

        }

        text = log.lower()

        # --------------------------
        # Detect stack trace
        # --------------------------

        exception = re.search(
            r"([\w\.]+(?:Exception|Error))",
            log
        )

        if exception:
            result["Exception Type"] = exception.group(1)

        failure = re.search(
            r'at (.+?\.\w+\(.+?:\d+\))',
            log
        )

        if failure:
            result["Failure Point"] = failure.group(1)

        path = re.findall(
            r'at (.+?\.\w+\(.+?\))',
            log
        )

        if path:
            result["Affected Code Path"] = path
        else:
            result["Affected Code Path"] = [
                "No stack trace detected."
            ]

        # --------------------------
        # Rule-based analysis
        # --------------------------

        for rule in self.rules:

            if any(keyword in text for keyword in rule["keywords"]):

                result["Exception Type"] = rule["exception"]

                if result["Failure Point"] == "Unknown":
                    result["Failure Point"] = rule["failure"]

                result["Likely Cause"] = rule["cause"]

                result["Confidence"] = rule["confidence"]

                if result["Affected Code Path"] == [
                    "No stack trace detected."
                ]:
                    result["Affected Code Path"] = [
                        rule["failure"]
                    ]

                break

        return result