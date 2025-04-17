import pandas as pd
import dask.dataframe as dd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

trips_full_pd = pd.read_csv('Trips_Full_Data.csv')
trips_distance_pd = pd.read_csv('Trips_by_distance.csv')
#Q1a How many people stayed at home:

total_staying_at_home = trips_full_pd['Population Staying at Home'].sum() 
print(f"Total population staying at home: {total_staying_at_home}") 

#Q1a Trips made by people not staying at home:
trips_by_people_not_staying_at_home = trips_full_pd['People Not Staying at Home'] * trips_full_pd.iloc[:, 6:].sum(axis=1)


trips_1_3_miles = trips_full_pd['Trips 1-3 Miles'] * trips_full_pd['People Not Staying at Home']
trips_3_5_miles = trips_full_pd['Trips 3-5 Miles'] * trips_full_pd['People Not Staying at Home']
trips_5_10_miles = trips_full_pd['Trips 5-10 Miles'] * trips_full_pd['People Not Staying at Home']
trips_10_25_miles = trips_full_pd['Trips 10-25 Miles'] * trips_full_pd['People Not Staying at Home']
trips_25_50_miles = trips_full_pd['Trips 25-50 Miles'] * trips_full_pd['People Not Staying at Home']
trips_50_100_miles = trips_full_pd['Trips 50-100 Miles'] * trips_full_pd['People Not Staying at Home']
trips_100_250_miles = trips_full_pd['Trips 100-250 Miles'] * trips_full_pd['People Not Staying at Home']
trips_250_500_miles = trips_full_pd['Trips 250-500 Miles'] * trips_full_pd['People Not Staying at Home']
trips_500_miles_plus = trips_full_pd['Trips 500+ Miles'] * trips_full_pd['People Not Staying at Home']

total_trips = {
    '1-3 Miles': trips_1_3_miles.sum(),
    '3-5 Miles': trips_3_5_miles.sum(),
    '5-10 Miles': trips_5_10_miles.sum(),
    '10-25 Miles': trips_10_25_miles.sum(),
    '25-50 Miles': trips_25_50_miles.sum(),
    '50-100 Miles': trips_50_100_miles.sum(),
    '100-250 Miles': trips_100_250_miles.sum(),
    '250-500 Miles': trips_250_500_miles.sum(),
    '500+ Miles': trips_500_miles_plus.sum()
}

#Plots the amount of trips done by ditance of trips.
distance_ranges = list(total_trips.keys())
trip_counts = list(total_trips.values())

plt.figure(figsize=(10, 6))
plt.bar(distance_ranges, trip_counts, color='purple')

plt.title("Total Trips Made by People Not Staying at Home per Distance Range")
plt.xlabel("Distance Range")
plt.ylabel("Total Number of Trips")
plt.xticks(rotation=45, ha='right')

formatter = FuncFormatter(lambda x, pos: f'{int(x):,}')  # Adds commas as thousands separators
plt.gca().yaxis.set_major_formatter(formatter)
plt.tight_layout()

plt.savefig('trips_plot.png')
plt.show()
