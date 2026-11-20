# ISM2411 Lab 13 - First DataFrame - Retail Sales Explorer
# Name: Tony Wiley
# 1. What does a boolean filter do?
# It checks every row against a True/False test, like "is the region South?"
# Then it keeps only the rows where the answer is True and drops the rest.

# 2. What is the difference between df["revenue"] and df[["revenue"]]?
# df["revenue"] gives back one column as a Series, which is basically a list of values.
# df[["revenue"]] gives back a DataFrame, which is a table that just has one column.
# It matters when the next step needs a table, like saving to CSV or adding more
# columns, or when you want to do math like .mean() on a single column (use the Series).

# 3. Why pick pandas over Excel for this?
# Pandas can handle huge files fast, and the code repeats the exact same steps
# every time with no clicking, so it's quicker and has fewer mistakes when the data changes.

import pandas as pd

#  Exercise 1: 
print("=== Exercise 1: Load it ===")
df = pd.read_csv("data/retail_sales.csv")
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.dtypes)

# Exercise 2: 
print("\n=== Exercise 2: Filter by region ===")
south = df[df["region"] == "South"]
print("South rows:", len(south))
print(south.head())

#  Exercise 3: 
print("\n=== Exercise 3: Top 5 by revenue ===")
top5 = df.sort_values("revenue", ascending=False).head(5)
print(top5)
# The index numbers on the left are not 0-4 because we did not reset the index.

# Exercise 4: 
print("\n=== Exercise 4: Two-condition filter ===")
big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]
print("South rows with revenue > 1000:", len(big_south))
print(big_south.head())

#  Exercise 5:
print("\n=== Exercise 5: A new column ===")
df["per_unit"] = df["revenue"] / df["quantity"]
print(df.head())
print("Mean per-unit price:", df["per_unit"].mean())

#  Exercise 6: 
print("\n=== Exercise 6: Unique values ===")
print(df["region"].unique())
print(df["region"].value_counts(dropna=False))

#  Exercise 7: 
print("\n=== Exercise 7: Select columns ===")
subset = df[["region", "product", "revenue"]]
print("Subset shape:", subset.shape)
# Picking only the columns you need uses less memory and keeps the analysis focused.

#  Exercise 8: 
print("\n=== Exercise 8: Save ===")
df.to_csv("data/explored.csv", index=False)
print("Saved data/explored.csv")