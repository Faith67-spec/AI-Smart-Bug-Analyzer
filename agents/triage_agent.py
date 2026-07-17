import re


class TriageAgent:

    def __init__(self):

        self.rules = [

            {
                "keywords": [
                    "nullpointerexception"
                ],
                "severity": "Critical",
                "priority": "P1",
                "confidence": 98,
                "component": "Backend",
                "reason":
                "A NullPointerException indicates an unexpected application crash caused by a null object reference."
            },

            {
                "keywords": [
                    "outofmemoryerror",
                    "memory leak"
                ],
                "severity": "Critical",
                "priority": "P1",
                "confidence": 97,
                "component": "Memory",
                "reason":
                "The application exhausted available memory, preventing normal execution."
            },

            {
                "keywords": [
                    "cannotgetjdbcconnectionexception",
                    "sqlexception",
                    "database connection"
                ],
                "severity": "High",
                "priority": "P2",
                "confidence": 95,
                "component": "Database",
                "reason":
                "The application cannot establish communication with the database."
            },

            {
                "keywords": [
                    "sqlsyntaxerrorexception",
                    "sql syntax"
                ],
                "severity": "Medium",
                "priority": "P3",
                "confidence": 90,
                "component": "Database",
                "reason":
                "An invalid SQL query prevented successful execution."
            },

            {
                "keywords": [
                    "login",
                    "authentication",
                    "invalid credentials",
                    "password reset"
                ],
                "severity": "High",
                "priority": "P2",
                "confidence": 92,
                "component": "Authentication",
                "reason":
                "Authentication failures prevent users from accessing the application."
            },

            {
                "keywords": [
                    "payment",
                    "transaction failed"
                ],
                "severity": "High",
                "priority": "P2",
                "confidence": 94,
                "component": "Payment",
                "reason":
                "Payment processing failed, impacting financial transactions."
            },

            {
                "keywords": [
                    "connectexception",
                    "connection refused",
                    "network"
                ],
                "severity": "High",
                "priority": "P2",
                "confidence": 91,
                "component": "Network",
                "reason":
                "The application failed to establish a network connection."
            },

            {
                "keywords": [
                    "timeout",
                    "timeoutexception"
                ],
                "severity": "Medium",
                "priority": "P3",
                "confidence": 88,
                "component": "API",
                "reason":
                "A request exceeded the configured response timeout."
            },

            {
                "keywords": [
                    "permission denied",
                    "accessdeniedexception",
                    "unauthorized"
                ],
                "severity": "Medium",
                "priority": "P3",
                "confidence": 89,
                "component": "Security",
                "reason":
                "The user lacks sufficient permissions to perform the requested action."
            },

            {
                "keywords": [
                    "filenotfoundexception",
                    "ioexception",
                    "file not found"
                ],
                "severity": "Medium",
                "priority": "P3",
                "confidence": 87,
                "component": "File System",
                "reason":
                "The application attempted to access a file that could not be located."
            },

            {
                "keywords": [
                    "http 500",
                    "internal server error"
                ],
                "severity": "High",
                "priority": "P2",
                "confidence": 90,
                "component": "Web Server",
                "reason":
                "The server encountered an unexpected condition while processing the request."
            },

            {
                "keywords": [
                    "indexoutofboundsexception"
                ],
                "severity": "Medium",
                "priority": "P3",
                "confidence": 89,
                "component": "Backend",
                "reason":
                "The application attempted to access an invalid array or list index."
            },

            {
                "keywords": [
                    "ui",
                    "frontend",
                    "render"
                ],
                "severity": "Low",
                "priority": "P4",
                "confidence": 80,
                "component": "User Interface",
                "reason":
                "The issue affects the user interface but does not stop core functionality."
            }

        ]

    def analyze(self, bug_report, log):

        text = (bug_report + "\n" + log).lower()

        result = {

            "Severity": "Low",
            "Priority": "P4",
            "Component": "General",
            "Confidence": 60,
            "Reasoning":
            "No known critical patterns were detected. The issue has been classified using the default rule."

        }

        for rule in self.rules:

            if any(keyword in text for keyword in rule["keywords"]):

                result = {

                    "Severity": rule["severity"],

                    "Priority": rule["priority"],

                    "Component": rule["component"],

                    "Confidence": rule["confidence"],

                    "Reasoning": rule["reason"]

                }

                break

        return result