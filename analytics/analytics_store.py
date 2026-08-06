import json
import os


class AnalyticsStore:

    def __init__(self):

        self.file_path = os.path.join(
            os.path.dirname(__file__),
            "analytics_data.json"
        )

        # Create the file if it doesn't exist
        if not os.path.exists(self.file_path):

            with open(self.file_path, "w") as f:

                json.dump([], f)

    def save_analysis(self, analysis):

        data = self.get_all_analyses()

        data.append(analysis)

        with open(self.file_path, "w") as f:

            json.dump(
                data,
                f,
                indent=4
            )

    def get_all_analyses(self):

        with open(self.file_path, "r") as f:

            return json.load(f)

    def clear(self):

        with open(self.file_path, "w") as f:

            json.dump([], f)