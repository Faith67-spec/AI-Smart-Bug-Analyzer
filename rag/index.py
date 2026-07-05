import chromadb
import pandas as pd
import numpy as np

print("Loading data...")

df = pd.read_csv("data/chunks.csv")

embeddings = np.load("data/embeddings.npy")

print("Connecting to ChromaDB...")

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="bug_reports"
)

print("Indexing vectors...")

for i in range(len(df)):

    collection.add(

        ids=[str(i)],

        documents=[df.iloc[i]["chunk"]],

        embeddings=[embeddings[i].tolist()],

        metadatas=[

            {

                "Bug_ID": str(df.iloc[i]["Bug ID"])

            }

        ]

    )

print()

print("Indexing Complete")

print()

print("Total Documents:")

print(collection.count())