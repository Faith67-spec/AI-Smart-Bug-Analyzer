class RecommendationAgent:

    def recommend(self, triage, log):

        exception = log["Exception Type"].lower()

        recommendations = []

        # -----------------------------------
        # Null Pointer Exception
        # -----------------------------------

        if "nullpointer" in exception:

            recommendations = [

                "Root Cause: Object reference was null before method invocation.",

                "Historical Resolution: Similar defects were resolved by initializing objects before use.",

                "Initialize objects before method invocation.",

                "Add null checks before accessing object members.",

                "Validate request parameters before processing.",

                "Review AuthenticationService login workflow.",

                "Engineering Best Practice: Use Optional objects or defensive programming to avoid null references."

            ]

        # -----------------------------------
        # Database Connection
        # -----------------------------------

        elif "jdbc" in exception or "connection" in exception:

            recommendations = [

                "Root Cause: Database connection could not be established.",

                "Historical Resolution: Similar issues were fixed by correcting JDBC configuration and restoring database availability.",

                "Verify database server availability.",

                "Check JDBC URL configuration.",

                "Validate database credentials.",

                "Inspect database connection pool settings.",

                "Engineering Best Practice: Implement retry mechanisms and health checks for database services."

            ]

        # -----------------------------------
        # Index Out Of Bounds
        # -----------------------------------

        elif (
            "indexoutofbounds" in exception
            or "arrayindexoutofbounds" in exception
        ):

            recommendations = [

                "Root Cause: Invalid collection index accessed.",

                "Historical Resolution: Similar defects were resolved by validating collection boundaries before access.",

                "Validate collection size before access.",

                "Add boundary checks.",

                "Review loop conditions.",

                "Handle empty collections safely.",

                "Engineering Best Practice: Include boundary condition tests in regression testing."

            ]

        # -----------------------------------
        # Access Denied
        # -----------------------------------

        elif (
            "accessdeniedexception" in exception
            or "permission denied" in exception
        ):

            recommendations = [

                "Root Cause: Application lacks permission to access the requested resource.",

                "Historical Resolution: Similar defects were resolved by correcting file permissions and deployment privileges.",

                "Verify file and folder permissions.",

                "Ensure the application has read/write privileges.",

                "Review operating system security policies.",

                "Check deployment user permissions.",

                "Engineering Best Practice: Apply the Principle of Least Privilege while granting required permissions."

            ]

        # -----------------------------------
        # File Not Found
        # -----------------------------------

        elif "filenotfoundexception" in exception:

            recommendations = [

                "Root Cause: Required file could not be located.",

                "Historical Resolution: Similar issues were resolved by correcting file paths and deployment artifacts.",

                "Verify the configured file path.",

                "Ensure required files exist.",

                "Validate deployment package contents.",

                "Use configurable resource paths.",

                "Engineering Best Practice: Validate file existence before opening resources."

            ]

        # -----------------------------------
        # IO Exception
        # -----------------------------------

        elif "ioexception" in exception:

            recommendations = [

                "Root Cause: File or stream input/output operation failed.",

                "Historical Resolution: Similar defects were resolved by improving file handling and resource cleanup.",

                "Verify file accessibility.",

                "Close streams properly.",

                "Handle disk I/O exceptions.",

                "Retry transient operations when appropriate.",

                "Engineering Best Practice: Use try-with-resources for automatic resource management."

            ]

        # -----------------------------------
        # Authentication Failure
        # -----------------------------------

        elif (
            "authentication" in exception
            or "invalid credentials" in exception
            or "login failed" in exception
        ):

            recommendations = [

                "Root Cause: User authentication failed because supplied credentials could not be validated.",

                "Historical Resolution: Similar authentication defects were resolved by validating credentials and reviewing authentication configuration.",

                "Verify username and password.",

                "Review authentication service configuration.",

                "Inspect password hashing implementation.",

                "Check account lockout and authorization policies.",

                "Engineering Best Practice: Implement secure authentication with comprehensive audit logging."

            ]

        # -----------------------------------
        # SQL Exception
        # -----------------------------------

        elif "sqlexception" in exception:

            recommendations = [

                "Root Cause: Database query execution failed.",

                "Historical Resolution: Similar SQL defects were resolved by correcting queries and validating database constraints.",

                "Review SQL syntax.",

                "Validate query parameters.",

                "Check database schema consistency.",

                "Inspect transaction handling.",

                "Engineering Best Practice: Use parameterized queries and proper exception handling."

            ]

        # -----------------------------------
        # Timeout
        # -----------------------------------

        elif (
            "timeoutexception" in exception
            or "sockettimeoutexception" in exception
            or "timed out" in exception
        ):

            recommendations = [

                "Root Cause: External service failed to respond within the timeout period.",

                "Historical Resolution: Similar issues were resolved by increasing timeout thresholds and optimizing service performance.",

                "Verify network connectivity.",

                "Increase timeout configuration where appropriate.",

                "Monitor external service availability.",

                "Implement retry policies.",

                "Engineering Best Practice: Use circuit breakers and exponential backoff for resilient communication."

            ]

        # -----------------------------------
        # Connection Refused
        # -----------------------------------

        elif "connection refused" in exception:

            recommendations = [

                "Root Cause: Remote service rejected the network connection.",

                "Historical Resolution: Similar defects were resolved by restoring service availability and correcting endpoint configuration.",

                "Verify target service is running.",

                "Check firewall configuration.",

                "Validate host and port settings.",

                "Inspect network routing.",

                "Engineering Best Practice: Monitor service availability using health checks."

            ]

        # -----------------------------------
        # Out Of Memory
        # -----------------------------------

        elif "outofmemoryerror" in exception:

            recommendations = [

                "Root Cause: JVM exhausted available heap memory.",

                "Historical Resolution: Similar defects were resolved by optimizing memory usage and increasing JVM heap size.",

                "Review memory-intensive operations.",

                "Analyze heap dumps.",

                "Increase JVM heap allocation.",

                "Investigate potential memory leaks.",

                "Engineering Best Practice: Profile memory usage during performance testing."

            ]

        # -----------------------------------
        # Illegal Argument
        # -----------------------------------

        elif "illegalargumentexception" in exception:

            recommendations = [

                "Root Cause: Invalid method argument supplied.",

                "Historical Resolution: Similar defects were resolved by validating user input before processing.",

                "Validate all input parameters.",

                "Review API contracts.",

                "Add defensive validation.",

                "Improve exception handling.",

                "Engineering Best Practice: Validate inputs at application boundaries."

            ]

        # -----------------------------------
        # Default
        # -----------------------------------

        else:

            recommendations = [

                "Root Cause: Unable to determine automatically.",

                "Review the complete stack trace.",

                "Inspect recent commits.",

                "Improve exception handling.",

                "Increase application logging.",

                "Engineering Best Practice: Add regression tests after resolving the defect."

            ]

        return recommendations