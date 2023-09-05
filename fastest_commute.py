#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import os

def determine_fastest_route(csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Separate data for Route 0 and Route 1
    # route 0 = vippa, route 1 = kvadraturen
    route_0_times = df[df['Route'] == 0]['Time']
    route_1_times = df[df['Route'] == 1]['Time']

    # Perform the independent two-sample t-test
    t_stat, p_value = ttest_ind(route_0_times, route_1_times)

    # Define the significance level (e.g., 0.05 for a 5% significance level)
    significance_level = 0.05

    # Determine the fastest route based on the p-value
    if p_value < significance_level:
        if t_stat < 0:
            fastest_route = "Route 0 (Vippa)"
            slower_route = "Route 1 (Kvadraturen)"
        else:
            fastest_route = "Route 1 (Kvadraturen)"
            slower_route = "Route 0 (Vippa)"
        print(f"The fastest route is {fastest_route}.")
    else:
        print("There is no significant difference in commute times between the two routes.")
        print("p = " + str(p_value))

    # Plot commute time for each route
    plt.figure(figsize=(10, 6))
    plt.boxplot([route_0_times, route_1_times], labels=['Vippa', 'Kvadraturen'])
    plt.xlabel('Route')
    plt.ylabel('Commute Time (seconds)')
    plt.title('Commute Time Comparison between Vippa and Kvadraturen')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = "./file.csv"  # Replace this with the actual path to your CSV file
    csv_file_path = os.path.join(script_dir, 'file.csv')
    determine_fastest_route(csv_file_path)

