import pandas as pd
'''In Pandas, both merge() and join() are used to combine two DataFrames, but they work differently.
1. merge()
merge() is used to combine DataFrames using common columns or indexes.
It works like SQL joins and supports different join types such as inner, left, right, and outer.'''

def merge_example():
    df1 = pd.DataFrame({"id": [1, 2, 3], "name": ["A", "B", "C"]})
    df2 = pd.DataFrame({"id": [2, 3, 4], "city": ["Delhi", "Mumbai", "Pune"]})
    return pd.merge(df1, df2, on="id", how="inner")


'''2. join()
join() is used to combine DataFrames using their index.
By default, it performs a left join and has a simpler syntax. '''


def join_example():
    df1 = pd.DataFrame({"Name": ["A", "B", "C"]}, index=[1, 2, 3])
    df2 = pd.DataFrame({"City": ["Delhi", "Mumbai", "Pune"]}, index=[2, 3, 4])
    return df1.join(df2)
