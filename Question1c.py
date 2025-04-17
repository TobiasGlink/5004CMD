import pandas as pd
import dask.dataframe as dd
import time
from dask.distributed import Client

# Setup Dask client for monitoring
client = Client()

# Load data with Pandas 
start_time = time.time()
trips_full_pd = pd.read_csv('Trips_Full_Data.csv')
trips_distance_pd = pd.read_csv('Trips_by_distance.csv')
end_time = time.time()
pandas_time = end_time - start_time
print(f"Time taken with Pandas: {pandas_time:.2f} seconds")

# Dask with default partitioning
start_time = time.time()
trips_full = dd.read_csv('Trips_Full_Data.csv')
trips_distance = dd.read_csv('Trips_by_distance.csv')
end_time = time.time()
dask_default_time = end_time - start_time
print(f"Time taken with Dask (default partitioning): {dask_default_time:.2f} seconds")

# Dask with  10 partitions
start_time = time.time()
trips_full_partitioned = dd.read_csv('Trips_Full_Data.csv', blocksize='64MB')  # Set blocksize to control partitions
trips_distance_partitioned = dd.read_csv('Trips_by_distance.csv', blocksize='64MB')
end_time = time.time()
dask_partitioned_time = end_time - start_time
print(f"Time taken with Dask (10 partitions): {dask_partitioned_time:.2f} seconds")

client.run_on_scheduler(lambda dask_scheduler: dask_scheduler.dashboard_link)
