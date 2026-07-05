import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
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