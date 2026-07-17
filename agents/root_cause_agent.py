class RootCauseAgent:

    def analyze(self, bug_report, log):

        text = (bug_report + "\n" + log).lower()

        if "nullpointerexception" in text:

            return {
                "Root Cause":
                "The application attempted to access an object that had not been initialized before use.",

                "Technical Explanation":
                "The User object was null when getUsername() was called during the login process.",

                "Affected Module":
                "Authentication Module"
            }

        elif "jdbc" in text or "connection" in text:

            return {
                "Root Cause":
                "The application could not establish a database connection.",

                "Technical Explanation":
                "The authentication service failed because the database server was unavailable or the JDBC configuration was incorrect.",

                "Affected Module":
                "Database Layer"
            }

        elif "indexoutofboundsexception" in text:

            return {
                "Root Cause":
                "The application attempted to access an invalid index in a collection.",

                "Technical Explanation":
                "A list or array was accessed outside its valid range.",

                "Affected Module":
                "Collection Processing"
            }

        else:

            return {
                "Root Cause":
                "Unable to determine the exact cause.",

                "Technical Explanation":
                "Additional logs or historical defects are required for deeper analysis.",

                "Affected Module":
                "Unknown"
            }