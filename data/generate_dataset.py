import pandas as pd

universities = [
    [1,"MIT","USA","Top university for artificial intelligence machine learning robotics and computer science research"],
    [2,"Stanford","USA","Strong computer science entrepreneurship and startup ecosystem"],
    [3,"CMU","USA","Leading university for artificial intelligence software engineering and robotics"],
    [4,"UC Berkeley","USA","Excellent machine learning data science and AI programs"],
    [5,"Georgia Tech","USA","Affordable engineering and computer science education"],
    [6,"Waterloo","Canada","Known for computer science and cooperative education programs"],
    [7,"University of Toronto","Canada","Strong artificial intelligence and research opportunities"],
    [8,"ETH Zurich","Switzerland","World class engineering and computer science university"],
    [9,"Oxford","UK","Research intensive university with strong technology programs"],
    [10,"Cambridge","UK","Leading institution for engineering and computer science"]
]

df = pd.DataFrame(
    universities,
    columns=["id","name","country","description"]
)

df.to_csv("data/universities.csv", index=False)

print("Dataset created successfully!")
