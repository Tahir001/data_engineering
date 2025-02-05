import pandas as pd
df = pd.read_csv("wine_data.csv")
print(df.head)
print("---------------------")

# GEt schema
print(df.info())