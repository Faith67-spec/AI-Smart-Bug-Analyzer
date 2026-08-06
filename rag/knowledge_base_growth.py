import os
import uuid

import chromadb
from sentence_transformers import SentenceTransformer


class KnowledgeBaseGrowth:

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

        self.client = chromadb.PersistentClient(
            path=db_path
        )

        self.collection = self.client.get_collection(
            "bug_reports"
        )

    def add_resolved_bug(
        self,
        bug_report,
        severity,
        component,
        root_cause,
        confidence,
        recommendations
    ):

        document = f"""
Bug Report:
{bug_report}

Severity:
{severity}

Component:
{component}

Root Cause:
{root_cause}

Confidence:
{confidence}

Resolution:
{recommendations}
"""

        embedding = self.model.encode(document)

        self.collection.add(

            ids=[str(uuid.uuid4())],

            documents=[document],

            embeddings=[embedding.tolist()],

            metadatas=[

                {

                    "Bug_ID": "User_Submitted",

                    "Status": "Resolved",

                    "Severity": severity,

                    "Component": component,

                    "Root_Cause": root_cause,

                    "Confidence": confidence

                }

            ]

        )

        print("✅ New resolved bug added to ChromaDB.")