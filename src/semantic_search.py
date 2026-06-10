import os

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

model = SentenceTransformer(
    "paraphrase-MiniLM-L3-v2"
)

while True:

    query = input("\nSearch (or type exit): ")

    if query.lower() == "exit":
        break

    query_vector = model.encode(query).tolist()

    results = client.query_points(
        collection_name="universities",
        query=query_vector,
        limit=5
    )

    print("\nTop Results:\n")

    for point in results.points:

        print(
            f"{point.payload['name']} "
            f"({point.payload['country']})"
        )
        