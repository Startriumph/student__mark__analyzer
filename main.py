import pandas as pd

df = pd.read_csv("studentmarks.csv")

df["Average"] = (df["Math"] + df["Science"] + df["English"] + df["SecondLang"]) / 4

topper = df.loc[df["Average"].idxmax()]

print("Student Data:")
print(df)

print("\nTopper:")
print(topper["Name"], "-", topper["Average"])

print("\nSubject-wise Highest Marks:")
print("Math:", df["Math"].max())
print("Science:", df["Science"].max())
print("English:", df["English"].max())
print("Second Language:", df["SecondLang"].max())
