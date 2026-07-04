import pandas as pd

df = pd.read_csv("data/processed.csv")

chunks = []
bug_ids = []

for _, row in df.iterrows():

    text = str(row["text"])

    bug_id = row["Bug ID"]

    chunk_size = 500

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

        bug_ids.append(bug_id)

chunk_df = pd.DataFrame({

    "Bug ID": bug_ids,

    "chunk": chunks

})

chunk_df.to_csv(

    "data/chunks.csv",

    index=False

)

print("\nChunking Complete")

print("Total Chunks Created:", len(chunk_df))