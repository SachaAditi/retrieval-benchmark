import pandas as pd

universities = []

topics = [
    "artificial intelligence",
    "machine learning",
    "robotics",
    "data science",
    "entrepreneurship",
    "computer science",
    "software engineering",
    "innovation",
    "deep learning",
    "autonomous systems"
]

for i in range(1, 101):

    universities.append([
        i,
        f"University_{i}",
        "USA",
        f"Leading institution for {topics[i % len(topics)]} research, startup ecosystem, innovation, engineering education and technology development."
    ])

df = pd.DataFrame(
    universities,
    columns=[
        "id",
        "name",
        "country",
        "description"
    ]
)

df.to_csv(
    "data/universities_large.csv",
    index=False
)

print("Created 100 universities")
