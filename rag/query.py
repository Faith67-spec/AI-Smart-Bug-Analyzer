import os
import chromadb
from sentence_transformers import SentenceTransformer


class BugQuery:

    def __init__(self):

        self.model = SentenceTransformer(
            r"C:\Users\HomePC\.cache\huggingface\hub\models--sentence-transformers--all-MiniLM-L6-v2\snapshots\1110a243fdf4706b3f48f1d95db1a4f5529b4d41",
            local_files_only=True
        )

        base_dir = os.path.dirname(__file__)

        db_path = os.path.join(
            base_dir,
            "chroma_db"
        )

        client = chromadb.PersistentClient(
            path=db_path
        )

        self.collection = client.get_collection(
            "bug_reports"
        )

    def search(self, query, top_k=3):

        embedding = self.model.encode(query)

        results = self.collection.query(
            query_embeddings=[embedding.tolist()],
            n_results=top_k,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

        similar_bugs = []

        for i in range(len(results["documents"][0])):

            distance = results["distances"][0][i]

            similarity = round(
                100 / (1 + distance),
                2
            )

            similar_bugs.append({

                "Bug": results["documents"][0][i],

                "Metadata": results["metadatas"][0][i],

                "Similarity": similarity

            })

        # Sort from highest similarity to lowest
        similar_bugs = sorted(
            similar_bugs,
            key=lambda x: x["Similarity"],
            reverse=True
        )

        return similar_bugs