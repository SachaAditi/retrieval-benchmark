import pandas as pd

from sentence_transformers import SentenceTransformer

# Load dataset
df = pd.read_csv("data/universities.csv")

# Load embedding model
model = SentenceTransformer(
    "paraphrase-MiniLM-L3-v2"
)

# Generate embeddings
embeddings = model.encode(
    df["description"].tolist()
)

print("Embedding shape:")
print(embeddings.shape)

print("\nFirst university:")
print(df.iloc[0]["name"])
