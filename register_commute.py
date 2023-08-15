#!/usr/bin/env python3

import csv
from datetime import datetime
import inquirer
import subprocess
import os

def get_user_input(prompt):
    return input(prompt).strip()

def parse_time_input(time_input):
    try:
        minutes, seconds = map(int, time_input.split(":"))
        if minutes < 0 or seconds < 0 or seconds >= 60:
            raise ValueError()
        return minutes * 60 + seconds
    except ValueError:
        print("Invalid time format. Please use the format 'm:ss'.")
        return None

def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')


def map_route_to_value(route):
    return 0 if route.lower() == 'vippa' else 1

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    date_input = get_user_input("Enter the date (YYYY-MM-DD) [default: today]: ")
    date = date_input if date_input else get_current_date()

    # Interactive route prompt
    questions = [
        inquirer.List('route',
                      message="Select the route:",
                      choices=['vippa', 'kvadraturen'],
                      ),
    ]
    route = inquirer.prompt(questions)['route']

    time_input = get_user_input("Enter the time taken (format m:ss): ")
    time = parse_time_input(time_input)
    while not time:
        time_input = get_user_input("Enter the time taken (format m:ss): ")
        time = parse_time_input(time_input)

    route_value = map_route_to_value(route)

    csv_file_path = os.path.join(script_dir, 'file.csv')
    # Append the values to the CSV file
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, lineterminator='\n')
        csv_writer.writerow([date, route_value, time])

    # Commit the changes to Git
    commit_message = f"registration for {date}"
    subprocess.run(["git", "add", "file.csv"], cwd=script_dir)
    subprocess.run(["git", "commit", "-m", commit_message], cwd=script_dir)


if __name__ == "__main__":
    main()

