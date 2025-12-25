import pandas as pd
# Create DataFrames
df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["A", "B", "C"]
})

df2 = pd.DataFrame({
    "id": [2, 3, 4],
    "city": ["Delhi", "Mumbai", "Pune"]
})

# Outer Join
result = pd.merge(df1, df2, on="id", how="outer")

print(result)
