import os
import pandas as pd

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

df = pd.read_csv("data/universities.csv")

model = SentenceTransformer(
    "paraphrase-MiniLM-L3-v2"
)

embeddings = model.encode(
    df["description"].tolist()
)

points = []

for i, row in df.iterrows():

    points.append(
        PointStruct(
            id=int(row["id"]),
            vector=embeddings[i].tolist(),
            payload={
                "name": row["name"],
                "country": row["country"],
                "description": row["description"]
            }
        )
    )

client.upsert(
    collection_name="universities",
    points=points
)

print(f"Uploaded {len(points)} vectors!")