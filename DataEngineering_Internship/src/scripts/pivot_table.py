import pandas as pd

def pivot_table_example():
    data = {
        "Region": ["North", "North", "South", "South", "East", "West"],
        "Product": ["A", "B", "A", "B", "A", "B"],
        "Sales": [1000, 1500, 1200, 1800, 900, 1600]
    }
    df = pd.DataFrame(data)
    return pd.pivot_table(df, values="Sales", index="Region", aggfunc="sum")
