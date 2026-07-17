import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer(
    r"C:\Users\HomePC\.cache\huggingface\hub\models--sentence-transformers--all-MiniLM-L6-v2\snapshots\1110a243fdf4706b3f48f1d95db1a4f5529b4d41",
    local_files_only=True
)

print("Reading chunks...")

df = pd.read_csv(
    "data/chunks.csv"
)

texts = df["chunk"].tolist()

print("Generating embeddings...")

embeddings = model.encode(

    texts,

    show_progress_bar=True

)

np.save(

    "data/embeddings.npy",

    embeddings

)

print("\nEmbeddings saved successfully.")

print("Shape:")

print(embeddings.shape)