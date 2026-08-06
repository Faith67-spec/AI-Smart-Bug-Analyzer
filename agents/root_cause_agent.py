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

        # -------------------------------
        # Null Pointer
        # -------------------------------

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

        # -------------------------------
        # Access Denied
        # -------------------------------

        elif (
            "accessdeniedexception" in text
            or "permission denied" in text
        ):

            root_cause = (
                "The application attempted to access a protected "
                "file or directory without sufficient permissions."
            )

            explanation = (
                "The operating system denied access because the "
                "application lacks the required read or write "
                "permissions."
            )

            module = "File Security"

            confidence = 95

        # -------------------------------
        # File Not Found
        # -------------------------------

        elif "filenotfoundexception" in text:

            root_cause = (
                "The application attempted to access a file "
                "that could not be found."
            )

            explanation = (
                "The configured file path is invalid or the "
                "required file no longer exists."
            )

            module = "File System"

            confidence = 93

        # -------------------------------
        # IO Exception
        # -------------------------------

        elif "ioexception" in text:

            root_cause = (
                "An input/output operation failed while "
                "accessing system resources."
            )

            explanation = (
                "The application encountered an unexpected "
                "failure while reading or writing files."
            )

            module = "File System"

            confidence = 90

        # -------------------------------
        # Authentication Failure
        # -------------------------------

        elif (
            "authentication failed" in text
            or "invalid credentials" in text
            or "login failed" in text
        ):

            root_cause = (
                "User authentication failed because the supplied "
                "credentials could not be validated."
            )

            explanation = (
                "The authentication service rejected the username "
                "or password during login."
            )

            module = "Authentication Module"

            confidence = 94

        # -------------------------------
        # SQL Exception
        # -------------------------------

        elif "sqlexception" in text:

            root_cause = (
                "A database operation failed while executing "
                "an SQL query."
            )

            explanation = (
                "The SQL statement could not be completed because "
                "of a syntax error, constraint violation, or "
                "database issue."
            )

            module = "Database Layer"

            confidence = 93

        # -------------------------------
        # JDBC Connection
        # -------------------------------

        elif "jdbc" in text:

            root_cause = (
                "The application could not establish a "
                "database connection."
            )

            explanation = (
                "The authentication service failed because the "
                "database server was unavailable or the JDBC "
                "configuration was incorrect."
            )

            module = "Database Layer"

            confidence = 92

        # -------------------------------
        # Connection Refused
        # -------------------------------

        elif "connection refused" in text:

            root_cause = (
                "The target service refused the network connection."
            )

            explanation = (
                "The remote server is unavailable or is not "
                "accepting incoming connections."
            )

            module = "Network Layer"

            confidence = 92

        # -------------------------------
        # Timeout
        # -------------------------------

        elif (
            "timeoutexception" in text
            or "sockettimeoutexception" in text
            or "timed out" in text
        ):

            root_cause = (
                "The application exceeded the maximum waiting "
                "time while communicating with an external service."
            )

            explanation = (
                "The remote service did not respond before "
                "the timeout period expired."
            )

            module = "Network Communication"

            confidence = 91

        # -------------------------------
        # Index Out Of Bounds
        # -------------------------------

        elif (
            "indexoutofboundsexception" in text
            or "arrayindexoutofboundsexception" in text
        ):

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

        # -------------------------------
        # Illegal Argument
        # -------------------------------

        elif "illegalargumentexception" in text:

            root_cause = (
                "A method received an invalid or unsupported "
                "argument."
            )

            explanation = (
                "The application attempted to invoke a method "
                "using parameters outside the expected range."
            )

            module = "Input Validation"

            confidence = 91

        # -------------------------------
        # Out Of Memory
        # -------------------------------

        elif "outofmemoryerror" in text:

            root_cause = (
                "The Java Virtual Machine exhausted the "
                "available memory."
            )

            explanation = (
                "The application attempted to allocate more "
                "memory than the JVM heap could provide."
            )

            module = "Memory Management"

            confidence = 96

        # -------------------------------
        # Supporting Evidence
        # -------------------------------

        evidence = None

        if similar_bugs and len(similar_bugs) > 0:

            similarity = similar_bugs[0]["Similarity"]

            # Confidence adjustment using historical evidence

            if similarity >= 90:

                confidence = min(confidence + 4, 99)

            elif similarity >= 80:

                confidence = min(confidence + 3, 99)

            elif similarity >= 70:

                confidence = min(confidence + 2, 99)

            elif similarity >= 60:

                confidence = min(confidence + 1, 99)

            elif similarity < 50:

                confidence = max(confidence - 8, 55)

            else:

                confidence = max(confidence - 4, 60)

            # Only attach evidence when similarity is meaningful

            if similarity >= 60:

                evidence = {

                    "Similarity": similarity,

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