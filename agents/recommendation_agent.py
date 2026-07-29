class RecommendationAgent:

    def recommend(self, triage, log):

        exception = log["Exception Type"].lower()

        recommendations = []

        if "nullpointer" in exception:

            recommendations = [

                "Root Cause: Object reference was null before use.",

                "Historical Resolution: Similar defects were resolved by initializing objects before accessing their methods.",

                "Initialize objects before method invocation.",

                "Add null checks before accessing object members.",

                "Validate incoming request parameters.",

                "Review AuthenticationService login workflow.",

                "Engineering Best Practice: Add unit tests to cover null object scenarios."

            ]

        elif "jdbc" in exception or "connection" in exception:

            recommendations = [

                "Root Cause: Database connection could not be established.",

                "Historical Resolution: Similar issues were resolved by correcting the JDBC configuration and restoring database connectivity.",

                "Verify database server availability.",

                "Check JDBC URL configuration.",

                "Validate database credentials.",

                "Inspect connection pool settings.",

                "Engineering Best Practice: Monitor connection pool usage and implement retry logic."

            ]

        elif "indexoutofbounds" in exception:

            recommendations = [

                "Root Cause: Invalid collection index accessed.",

                "Historical Resolution: Similar defects were resolved by validating collection boundaries before access.",

                "Validate collection size before access.",

                "Add boundary checks.",

                "Review loop conditions.",

                "Handle empty collections safely.",

                "Engineering Best Practice: Include boundary condition tests in regression testing."

            ]

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