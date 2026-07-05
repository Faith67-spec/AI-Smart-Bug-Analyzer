import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    "bug_reports"
)

query = input("Enter bug description: ")

embedding = model.encode(
    query
)

results = collection.query(

    query_embeddings=[embedding.tolist()],

    n_results=5

)

print("\nMost Similar Historical Defects\n")

for i in range(

        len(results["documents"][0])

):

    print(

        f"\nResult {i+1}"

    )

    print(

        results["documents"][0][i]

    )

    print(

        results["metadatas"][0][i]

    )