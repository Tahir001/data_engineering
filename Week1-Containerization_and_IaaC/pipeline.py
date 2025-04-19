import pandas as pd
df = pd.read_csv("wine_data.csv")
print(df.head)
print("---------------------")
for i in range(10):
    time.sleep(10)
    print("I AM STILL ALIVE!")
    print(df.head)
# GEt schema
print(df.info())