import pandas as pd
import dask.dataframe as dd

trips_distance_pd = dd.read_csv('Trips_by_distance.csv')

over_10mil_10_25 = trips_distance[trips_distance["Number of Trips 10-25"] > 10000000][['Date']] 
over_10mil_50_100 = trips_distance[trips_distance["Number of Trips 50-100"] > 10000000][['Date']] 

df_10_25 = over_10mil_10_25.compute().drop_duplicates() 
df_50_100 = over_10mil_50_100.compute().drop_duplicates()

dates_10_25 = set(df_10_25['Date']) 
dates_50_100 = set(df_50_100['Date']) 

common_dates = dates_10_25.intersection(dates_50_100) 

only_10_25 = dates_10_25 - dates_50_100 
only_50_100 = dates_50_100 - dates_10_25 

print("Common Dates (Both thresholds met):", sorted(common_dates)) 
print("Only 10-25 Trips:", sorted(only_10_25)) 
print("Only 50-100 Trips:", sorted(only_50_100)) 
