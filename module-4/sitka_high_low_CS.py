# Colton Stone, November 9, 2025, Module 4.2 Assignment

# This program is made for a user to choose if they want to view the minimum or maximum parts of a temperature graph


import csv, sys
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # I added this function to allow the user to exit the program as well as display a goodbye message when the while loop terminates.
    def exitprogram():
        plt.close('all')
        print('\nYou have exited the weather menu.')
        sys.exit()



    # Get dates and high temperatures from this file.

    print("\nIn this program you will be selecting the temperature level that you want the weather graph to display.")
    while True:
        try:
            print("\nTo select the temperature type enter 'HIGH' for high temperatures, 'LOW' for low temperatures, or 'EXIT' to end the program.")
            menu = str(input("\nEnter your desired temperature level: "))
            if menu.upper() == 'EXIT':
                exitprogram()
            elif menu.upper() == 'HIGH':
                print("\nYou have selected to view the max temperature graphs ")
                dates, highs = [], []
                for row in reader:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    dates.append(current_date)
                    high = int(row[5])
                    highs.append(high)

                    # Plot the high temperatures.
                    # plt.style.use('seaborn')
                    fig, ax = plt.subplots()
                    ax.plot(dates, highs, c='red')

                    # Format plot.
                    plt.title("Daily high temperatures - 2018", fontsize=24)
                    plt.xlabel('', fontsize=16)
                    fig.autofmt_xdate()
                    plt.ylabel("Temperature (F)", fontsize=16)
                    plt.tick_params(axis='both', which='major', labelsize=16)
                    plt.show()
            elif menu.upper() == 'LOW':
                print("\nYou have selected to view the min temperature graphs ")
                dates, lows = [], []
                for row in reader:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    dates.append(current_date)
                    low = int(row[6])
                    lows.append(low)

                    fig, ax = plt.subplots()
                    ax.plot(dates, lows, c='blue')

                    # Format plot.
                    plt.title("Daily low temperatures - 2018", fontsize=24)
                    plt.xlabel('', fontsize=16)
                    fig.autofmt_xdate()
                    plt.ylabel("Temperature (F)", fontsize=16)
                    plt.tick_params(axis='both', which='major', labelsize=16)
                    plt.show()
            else:
                print('\nYou entered invalid input, please try again')

        # I was only able to end the matplotlib graph loops by terminating the program so when the program is stopped it will return to the
        # "exitprogram" function and display a message
        except KeyboardInterrupt:
            exitprogram()
