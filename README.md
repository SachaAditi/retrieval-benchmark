# Retrieval Benchmark: BM25 vs Vector Search

## Overview

This project compares traditional keyword-based retrieval (BM25) with semantic vector search using transformer embeddings and Qdrant Vector Database.

The goal is to evaluate how semantic search differs from keyword matching when retrieving relevant documents.

---

## Features

* BM25 keyword search
* Semantic vector search
* Qdrant Cloud integration
* Sentence Transformers embeddings
* Benchmark framework
* Retrieval performance comparison

---

## Project Structure

retrieval-benchmark/

├── data/

│ ├── universities.csv

│ ├── universities_large.csv

│ └── generate_large_dataset.py

├── src/

│ ├── bm25_search.py

│ ├── vector_search.py

│ ├── semantic_search.py

│ ├── qdrant_setup.py

│ ├── upload_vectors.py

│ ├── upload_large_dataset.py

│ └── benchmark.py

├── results/

│ └── benchmark_results.csv

├── requirements.txt

└── README.md

---

## Technologies Used

* Python
* Qdrant Cloud
* Sentence Transformers
* Pandas
* Rank-BM25
* GitHub Codespaces

---

## System Architecture

User Query

↓

Embedding Model

(paraphrase-MiniLM-L3-v2)

↓

384-Dimensional Vector

↓

Qdrant Vector Database

↓

Cosine Similarity Search

↓

Top-K Results

---

## Dataset

The project uses a synthetic university dataset containing institution descriptions related to:

* Artificial Intelligence
* Machine Learning
* Robotics
* Data Science
* Entrepreneurship
* Software Engineering
* Deep Learning
* Autonomous Systems

---

## Example Query

Query:

startup founders

Semantic Search Results:

* Stanford
* Waterloo
* Cambridge
* CMU
* Oxford

---

## Benchmark Goal

Compare:

1. BM25 keyword retrieval
2. Semantic vector retrieval

across multiple benchmark queries.

Example benchmark queries:

* startup founders
* robotics research
* machine learning
* innovation hub
* data analytics

---

## Future Improvements

* Larger datasets (1000+ documents)
* Hybrid search (BM25 + Vector Search)
* Retrieval accuracy metrics
* RAG integration
* ANN index comparison

---

## Author

Aditi Joshi

Internship Project – Vector Databases & Information Retrieval
