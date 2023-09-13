import csv
import sys
import os
from monthly_temperature import CheckMonthlyTemperature
from yearly_temperature import YearlyTemperature
from monthly_horizontal_chart import MonthlyChart

csv_read_array = []


def ReadFilesAsCSV(file_path):
    try:
        with open(
            file_path,
            "r",
        ) as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row == [] or len(row) == 1:
                    continue
                elif row[0].__contains__("PKT") or row[0].__contains__("PKST"):
                    max_temp_index = row.index("Max TemperatureC")
                    min_temp_index = row.index("Min TemperatureC")
                    mean_humidity_index = row.index(" Mean Humidity")
                    min_humidity_index = row.index(" Min Humidity")
                    max_humidity_index = row.index("Max Humidity")
                    date = (
                        row.index("PKT")
                        if row.__contains__("PKT")
                        else row.index("PKST")
                    )
                    continue
                else:
                    csv_read_array.append(row)

            return (
                max_temp_index,
                min_temp_index,
                max_humidity_index,
                date,
                mean_humidity_index,
                min_humidity_index,
            )
    except FileNotFoundError:
        print("Unable to locate file. Make sure that the path is correct")
        return
    except:
        print("Error occured while reading file")
        return


def DisplayYearResults(year, path):
    try:
        for file in os.listdir():
            if file.__contains__(year):
                file_path = f"{path}/{file}"

                (
                    max_temp_index,
                    min_temp_index,
                    max_humidity_index,
                    date,
                    mean_hum,
                    min_hum,
                ) = ReadFilesAsCSV(file_path)
                yearly_temperature = YearlyTemperature(csv_read_array)
                year_results = yearly_temperature.YearTemperature(
                    max_temp_index,
                    min_temp_index,
                    max_humidity_index,
                    date,
                    mean_hum,
                    min_hum,
                )
        print(
            "Highest: {}C on {}".format(
                year_results["max_temp"], year_results["pkt_max_temp"]
            )
        )
        print(
            "Lowest: {}C on {}".format(
                year_results["min_temp"], year_results["pkt_min_temp"]
            )
        )
        print(
            "Humid: {}% on {}".format(
                year_results["max_humidity"], year_results["pkt_humidity"]
            )
        )

    except FileNotFoundError:
        print(f"File with {year} doesn't exist")
        return


def DisplayMonth(month):
    monthly_temperature = CheckMonthlyTemperature(csv_read_array)
    month = monthly_temperature.CheckMonth(month)

    file_path = f"{path_to_file}/lahore_weather_{year}_{month}.txt"
    (
        max_temp_index,
        min_temp_index,
        max_humidity_index,
        date,
        mean_humidity_index,
        min_humidity_index,
    ) = ReadFilesAsCSV(file_path)

    highest_average = monthly_temperature.MonthTemperature(max_temp_index)
    lowest_average = monthly_temperature.MonthTemperature(min_temp_index)
    average_humidity = monthly_temperature.MonthTemperature(mean_humidity_index)

    print(f"Highest Average: {highest_average}C")
    print(f"Lowesr Average: {lowest_average}C")
    print(f"Average Humidity: {average_humidity}%")


def DisplayMonthlyChart(year, month):
    monthly_tem = CheckMonthlyTemperature()
    getMonth = monthly_tem.CheckMonth(month)
    try:
        file_path = f"{path_to_file}/lahore_weather_{year}_{getMonth}.txt"
        (
            max_temp_index,
            min_temp_index,
            max_humidity_index,
            date,
            mean,
            min,
        ) = ReadFilesAsCSV(file_path)

        print(f"\n{getMonth} {year}")
        monthly_chart = MonthlyChart(csv_read_array)
        monthly_chart.GetResults(max_temp_index, min_temp_index)

        print(f"\nBonus Task\n\n{getMonth} {year}")

        monthly_chart.GetResults(max_temp_index, min_temp_index, True)
    except:
        print("An error occured while reading file")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        command = sys.argv[1]
        year_res = sys.argv[2]
        path_to_file = sys.argv[3]

        if command == "-a":
            try:
                year_month = year_res.split("/")
                year = int(year_month[0])
                month = int(year_month[1])
                if month in range(1, 13):
                    DisplayMonth(month)
                else:
                    print("Please enter a valid month number")

            except IndexError:
                print("Usage: python weatherman.py -a 2005/12 /path/to/files")

        elif command == "-e":
            os.chdir(path_to_file)
            DisplayYearResults(year_res[:4], path_to_file)

        elif command == "-c":
            try:
                year_month = year_res.split("/")
                year = year_month[0]
                month = int(year_month[1])

                if month in range(1, 13):
                    DisplayMonthlyChart(year, month)
                else:
                    print("Please enter a valid month number")
            except IndexError:
                print("Usage: python weatherman.py -c 2005/12 /path/to/files")

        else:
            print("Invalid argument.")

    else:
        print("Invalid Command\nUsage: python weatherman.py -a 2005/8 /path/to/files")
