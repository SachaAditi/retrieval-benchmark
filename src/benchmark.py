import pandas as pd

queries = [
    "startup founders",
    "artificial intelligence",
    "robotics research",
    "machine learning",
    "engineering education",
    "autonomous robots",
    "innovation hub",
    "data analytics",
]

results = []

for query in queries:
    results.append({
        "Query": query,
        "BM25_Top_Result": "",
        "Vector_Top_Result": ""
    })

df = pd.DataFrame(results)

df.to_csv(
    "results/benchmark_results.csv",
    index=False
)

print(df)
print("\nBenchmark template created!")