class RootCauseAgent:

    def analyze(self, bug_report, log, similar_bugs=None):

        text = (bug_report + "\n" + log).lower()

        confidence = 70
        root_cause = "Unable to determine the exact cause."
        explanation = (
            "Additional logs or historical defects are required "
            "for deeper analysis."
        )
        module = "Unknown"

        if "nullpointerexception" in text:

            root_cause = (
                "The application attempted to access an object "
                "that had not been initialized."
            )

            explanation = (
                "The User object was null when getUsername() "
                "was invoked during authentication."
            )

            module = "Authentication Module"
            confidence = 96

        elif "jdbc" in text or "connection" in text:

            root_cause = (
                "The application could not establish a "
                "database connection."
            )

            explanation = (
                "The authentication service failed because "
                "the database server was unavailable or the "
                "JDBC configuration was incorrect."
            )

            module = "Database Layer"
            confidence = 92

        elif "indexoutofboundsexception" in text:

            root_cause = (
                "The application attempted to access an "
                "invalid collection index."
            )

            explanation = (
                "A list or array was accessed outside "
                "its valid range."
            )

            module = "Collection Processing"
            confidence = 90

        evidence = None

        if similar_bugs and len(similar_bugs) > 0:

            evidence = {

                "Similarity":
                    similar_bugs[0]["Similarity"],

                "Historical Bug":
                    similar_bugs[0]["Bug"]

            }

        return {

            "Root Cause": root_cause,

            "Confidence": confidence,

            "Technical Explanation": explanation,

            "Affected Module": module,

            "Supporting Evidence": evidence

        }