from rag.query import BugQuery


class DuplicateDetectionAgent:

    def __init__(self):

        self.query = BugQuery()

    def detect(self, bug_report):

        return self.query.search(
            bug_report,
            top_k=3
        )