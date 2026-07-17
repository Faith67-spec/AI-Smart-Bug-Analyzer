import os
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class BugRetriever:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        BASE_DIR = os.path.dirname(__file__)

        embeddings_path = os.path.join(
            BASE_DIR,
            "data",
            "embeddings.npy"
        )

        chunks_path = os.path.join(
            BASE_DIR,
            "data",
            "chunks.csv"
        )

        self.embeddings = np.load(
            embeddings_path
        )

        self.df = pd.read_csv(
            chunks_path
        )

    def retrieve(self, query, top_k=3):

        query_embedding = self.model.encode(
            [query]
        )

        similarities = cosine_similarity(
            query_embedding,
            self.embeddings
        )[0]

        top_indices = similarities.argsort()[-top_k:][::-1]

        results = []

        for idx in top_indices:

            results.append({

                "Bug": self.df.iloc[idx]["chunk"],

                "Similarity": round(
                    float(similarities[idx]) * 100,
                    2
                )

            })

        return results