import re


class LogAnalysisAgent:

    def analyze(self, log):

        result = {
            "Exception Type": "Unknown",
            "Failure Point": "Unknown",
            "Affected Code Path": [],
            "Likely Cause": "Unable to determine"
        }

        # -----------------------------
        # Exception Type
        # -----------------------------
        exception = re.search(
            r"([\w\.]+(?:Exception|Error))",
            log
        )

        if exception:
            result["Exception Type"] = exception.group(1)

        # -----------------------------
        # Failure Point
        # -----------------------------
        failure = re.search(
            r'at (.+?\.\w+\(.+?:\d+\))',
            log
        )

        if failure:
            result["Failure Point"] = failure.group(1)

        # -----------------------------
        # Code Path
        # -----------------------------
        path = re.findall(
            r'at (.+?\.\w+\(.+?\))',
            log
        )

        result["Affected Code Path"] = path

        # -----------------------------
        # Likely Cause
        # -----------------------------
        text = log.lower()

        if "nullpointerexception" in text:
            result["Likely Cause"] = (
                "Object was not initialized before use."
            )

        elif "cannotgetjdbcconnectionexception" in text:
            result["Likely Cause"] = (
                "Unable to establish database connection."
            )

        elif "indexoutofboundsexception" in text:
            result["Likely Cause"] = (
                "Array/List index exceeded its valid range."
            )

        elif "outofmemoryerror" in text:
            result["Likely Cause"] = (
                "Application exhausted available memory."
            )

        return result


if __name__ == "__main__":

    sample_log = """
    java.lang.NullPointerException

    at com.smartbug.auth.UserController.login(UserController.java:42)

    at com.smartbug.auth.AuthenticationService.authenticate(AuthenticationService.java:88)

    at org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:1071)
    """

    agent = LogAnalysisAgent()

    output = agent.analyze(sample_log)

    print("\n========== LOG ANALYSIS ==========\n")

    for key, value in output.items():

        if isinstance(value, list):

            print(key + ":")

            for item in value:
                print("  ->", item)

        else:

            print(f"{key}: {value}")