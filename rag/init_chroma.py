import os
import chromadb
import pandas as pd
import numpy as np


def initialize_chroma():

    base_dir = os.path.dirname(__file__)

    db_path = os.path.join(
        base_dir,
        "chroma_db"
    )

    chunks_path = os.path.join(
        base_dir,
        "data",
        "chunks.csv"
    )

    embeddings_path = os.path.join(
        base_dir,
        "data",
        "embeddings.npy"
    )

    client = chromadb.PersistentClient(
        path=db_path
    )

    collection = client.get_or_create_collection(
        name="bug_reports"
    )

    # Do not add the records again if the collection
    # is already populated.
    if collection.count() > 0:
        return collection

    df = pd.read_csv(chunks_path)

    embeddings = np.load(
        embeddings_path
    )

    ids = [
        str(i)
        for i in range(len(df))
    ]

    documents = df["chunk"].tolist()

    metadatas = [
        {
            "Bug_ID": str(row["Bug ID"])
        }
        for _, row in df.iterrows()
    ]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    return collection