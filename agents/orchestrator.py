from agents.triage_agent import TriageAgent
from agents.log_analysis_agent import LogAnalysisAgent
from agents.recommendation_agent import RecommendationAgent
from agents.root_cause_agent import RootCauseAgent
from agents.duplicate_detection_agent import DuplicateDetectionAgent
class BugAnalysisOrchestrator:

    def __init__(self):

        self.triage = TriageAgent()

        self.log_agent = LogAnalysisAgent()
        self.duplicate_detector = DuplicateDetectionAgent()
        self.recommendation = RecommendationAgent()
        self.root_cause = RootCauseAgent()
    def analyze(self, bug_report, log):

        # Run Triage Agent
        triage_result = self.triage.analyze(
            bug_report,
            log
        )

        # Run Log Analysis Agent
        combined_text = bug_report + "\n" + log

        log_result = self.log_agent.analyze(
    combined_text
)
        # Run Recommendation Agent
        recommendations = self.recommendation.recommend(
            triage_result,
            log_result
        )
        root_cause = self.root_cause.analyze(
             bug_report,
             log
       
)
        similar_bugs = self.duplicate_detector.detect(
     bug_report
)

        return {

    "Triage": triage_result,

    "Log Analysis": log_result,

    "Recommendations": recommendations,

    "Root Cause": root_cause,

    "Similar Bugs": similar_bugs

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