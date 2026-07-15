from agents.triage_agent import TriageAgent
from agents.log_analysis_agent import LogAnalysisAgent


class BugAnalysisOrchestrator:

    def __init__(self):

        self.triage = TriageAgent()

        self.log_agent = LogAnalysisAgent()

    def analyze(self, bug_report, log):

        triage_result = self.triage.analyze(
            bug_report,
            log
        )

        log_result = self.log_agent.analyze(
            log
        )

        return {

            "Triage": triage_result,

            "Log Analysis": log_result

        }


if __name__ == "__main__":

    bug = """
    Application crashes during login after entering valid credentials.
    """

    log = """
    java.lang.NullPointerException

    at com.smartbug.auth.UserController.login(UserController.java:42)

    at com.smartbug.auth.AuthenticationService.authenticate(AuthenticationService.java:88)

    at org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:1071)
    """

    orchestrator = BugAnalysisOrchestrator()

    results = orchestrator.analyze(
        bug,
        log
    )

    print("\n========== TRIAGE ==========\n")

    for key, value in results["Triage"].items():

        print(f"{key}: {value}")

    print("\n========== LOG ANALYSIS ==========\n")

    for key, value in results["Log Analysis"].items():

        print(f"{key}: {value}")