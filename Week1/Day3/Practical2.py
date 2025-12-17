import pandas as pd

# Sample sales data
data = {
    "Region": ["North", "North", "South", "South", "East", "West"],
    "Product": ["A", "B", "A", "B", "A", "B"],
    "Sales": [1000, 1500, 1200, 1800, 900, 1600]
}

df = pd.DataFrame(data)

# Create pivot table
pivot_table = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum"
)

print(pivot_table)
