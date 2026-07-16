class RecommendationAgent:

    def recommend(self, triage, log):

        exception = log["Exception Type"].lower()

        recommendations = []

        if "nullpointer" in exception:

            recommendations = [

                "Initialize objects before method invocation.",

                "Add null checks before accessing object members.",

                "Validate request parameters.",

                "Review AuthenticationService login workflow.",

                "Write unit tests for login edge cases."

            ]

        elif "jdbc" in exception or "connection" in exception:

            recommendations = [

                "Verify database server availability.",

                "Check JDBC URL configuration.",

                "Validate database credentials.",

                "Inspect connection pool settings.",

                "Retry database connection after recovery."

            ]

        elif "indexoutofbounds" in exception:

            recommendations = [

                "Validate collection size before access.",

                "Add boundary checks.",

                "Review loop conditions.",

                "Handle empty collections safely.",

                "Create regression tests."

            ]

        else:

            recommendations = [

                "Review stack trace carefully.",

                "Inspect recent commits.",

                "Improve exception handling.",

                "Increase logging.",

                "Create regression tests."

            ]

        return recommendations