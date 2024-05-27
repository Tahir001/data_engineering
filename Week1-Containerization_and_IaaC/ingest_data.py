import pandas as pd
from sqlalchemy import create_engine

# URL of the Parquet file
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"

# Read the Parquet file into a DataFrame
df = pd.read_parquet(url, engine='pyarrow')

# Display the first few rows of the DataFrame
print(df.head())

connection_string = 'postgresql://root:root@localhost:5432/ny_taxi'

# Create SQLAlchemy engine
engine = create_engine(connection_string)

# Put data in the postgres SQL database 
df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')