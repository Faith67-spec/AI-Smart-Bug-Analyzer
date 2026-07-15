import re


class TriageAgent:

    def analyze(self, bug_report, log):

        text = (bug_report + "\n" + log).lower()

        severity = "Low"
        priority = "P4"
        component = "General"
        confidence = 60
        reasoning = []

        # ---------- Severity ----------

        if "nullpointerexception" in text:
            severity = "Critical"
            priority = "P1"
            confidence = 96
            reasoning.append(
                "Application crashed due to NullPointerException."
            )

        elif "cannotgetjdbcconnectionexception" in text:
            severity = "High"
            priority = "P2"
            confidence = 93
            reasoning.append(
                "Database connection failure detected."
            )

        elif "indexoutofboundsexception" in text:
            severity = "Medium"
            priority = "P3"
            confidence = 88
            reasoning.append(
                "Array/List index exceeded valid range."
            )

        elif "outofmemoryerror" in text:
            severity = "Critical"
            priority = "P1"
            confidence = 95
            reasoning.append(
                "System ran out of available memory."
            )

        # ---------- Component ----------

        if "login" in text or "authentication" in text:
            component = "Authentication"

        elif "database" in text or "jdbc" in text:
            component = "Database"

        elif "payment" in text:
            component = "Payment"

        elif "ui" in text:
            component = "User Interface"

        else:
            component = "General"

        return {

            "Severity": severity,

            "Priority": priority,

            "Component": component,

            "Confidence": confidence,

            "Reasoning": reasoning

        }


if __name__ == "__main__":

    bug = """
    Application crashes during login.
    """

    log = """
    java.lang.NullPointerException

    at UserController.login(UserController.java:42)
    """

    agent = TriageAgent()

    result = agent.analyze(
        bug,
        log
    )

    print(result)