import pandas as pd
from rank_bm25 import BM25Okapi

# Load dataset
df = pd.read_csv("data/universities.csv")

# Convert descriptions into documents
documents = df["description"].tolist()

# Tokenize
tokenized_docs = [
    doc.lower().split()
    for doc in documents
]

# Build BM25 index
bm25 = BM25Okapi(tokenized_docs)

while True:

    query = input("\nSearch (or type exit): ")

    if query.lower() == "exit":
        break

    scores = bm25.get_scores(
        query.lower().split()
    )

    top_indices = scores.argsort()[-5:][::-1]

    print("\nTop Results:")

    for idx in top_indices:
        print(
            f"- {df.iloc[idx]['name']} ({df.iloc[idx]['country']})"
        )
        