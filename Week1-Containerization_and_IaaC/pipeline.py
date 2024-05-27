import pandas as pd
df = pd.read_parquet("/Users/tahir/Desktop/Github/dataengineering/Week1-Containerization_and_IaaC/yellow_tripdata_2024-01.parquet")
print(df.head)
print("---------------------")

# GEt schema
print(pd.io.sql.get_schema(df, name="yellow_taxi_data"))