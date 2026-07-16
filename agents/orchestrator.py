from agents.triage_agent import TriageAgent
from agents.log_analysis_agent import LogAnalysisAgent
from agents.recommendation_agent import RecommendationAgent


class BugAnalysisOrchestrator:

    def __init__(self):

        self.triage = TriageAgent()

        self.log_agent = LogAnalysisAgent()

        self.recommendation = RecommendationAgent()

    def analyze(self, bug_report, log):

        # Run Triage Agent
        triage_result = self.triage.analyze(
            bug_report,
            log
        )

        # Run Log Analysis Agent
        log_result = self.log_agent.analyze(
            log
        )

        # Run Recommendation Agent
        recommendations = self.recommendation.recommend(
            triage_result,
            log_result
        )

        return {

            "Triage": triage_result,

            "Log Analysis": log_result,

            "Recommendations": recommendations

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

    print("\n========== RECOMMENDATIONS ==========\n")

    for item in results["Recommendations"]:

        print(f"- {item}")