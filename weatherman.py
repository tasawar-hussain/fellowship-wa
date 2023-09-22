import csv
import os
import sys

from data_analyzer import DataAnalyzer
from monthly_horizontal_chart import MonthlyWeatherVisualizer
from monthly_temperature import MonthlyWeatherAnalyzer
from yearly_temperature import YearWeatherAnalyzer


def display_year_data(year, path):
    try:
        for file in os.listdir(path):
            if file.__contains__(year):
                file_path = f"{path}/{file}"

                analyzer = DataAnalyzer()
                data_list = analyzer.read_file_as_csv(file_path)
                max_temp_index, min_temp_index,  mean_humidity_index, max_humidity_index, date = get_header_value_index(file_path)
                
                year_data_handler = YearWeatherAnalyzer(data_list)
                data_dict = year_data_handler.year_analyzer(max_temp_index, min_temp_index, max_humidity_index, date, mean_humidity_index)
                
        print("Highest: {}C on {}".format(data_dict["max_temp"], data_dict["pkt_max_temp"]))
        print("Lowest: {}C on {}".format(data_dict["min_temp"], data_dict["pkt_min_temp"]))
        print("Humid: {}% on {}".format(data_dict["max_humidity"], data_dict["pkt_humidity"]))

    except FileNotFoundError:
        print(f"File with {year} doesn't exist")
        return


def display_month_data(path_to_file, month, year):
    month = MonthlyWeatherAnalyzer().get_month_value(month)
    for file in os.listdir(path_to_file):
        if file.__contains__(year) and file.__contains__(month):
            file_path = f"{path_to_file}/{file}"

    analyzer = DataAnalyzer()
    data_list = analyzer.read_file_as_csv(file_path)
    max_temp_index, min_temp_index, mean_humidity_index, max_humd_idx, date  = get_header_value_index(file_path)

   
    monthly_temperature = MonthlyWeatherAnalyzer(data_list)
    highest_average = monthly_temperature.calculate_average_value(max_temp_index)
    lowest_average = monthly_temperature.calculate_average_value(min_temp_index)
    average_humidity = monthly_temperature.calculate_average_value(mean_humidity_index)

    print(f"Highest Average: {highest_average}C")
    print(f"Lowest Average: {lowest_average}C")
    print(f"Average Humidity: {average_humidity}%")


def display_monthly_chart_data(year, month, path_to_file):
    monthly_data_handler = MonthlyWeatherAnalyzer()
    month = monthly_data_handler.get_month_value(month)
    try:
        for file in os.listdir(path_to_file):
            if file.__contains__(year) and file.__contains__(month):
                file_path = f"{path_to_file}/{file}"
        
        analyzer = DataAnalyzer()
        data_list = analyzer.read_file_as_csv(file_path)
        max_temp_index, min_temp_index, mean_humidity_index, max_humidity_index, date = get_header_value_index(file_path)

        print(f"\n{month} {year}")
        monthly_chart = MonthlyWeatherVisualizer(data_list)
        monthly_chart.get_results(max_temp_index, min_temp_index)

        print(f"\nBonus Task\n{month} {year}")
        monthly_chart.get_results(max_temp_index, min_temp_index, True)
    except:
        print("An error occured while reading file")

def get_header_value_index(file_path):
    analyzer = DataAnalyzer()
    data_list = analyzer.read_file_as_csv(file_path)

    max_temp_index = analyzer.find_index_of_columns("Max TemperatureC")
    min_temp_index = analyzer.find_index_of_columns("Min TemperatureC")
    mean_humidity_index = analyzer.find_index_of_columns(" Mean Humidity")
    max_humidity_index = analyzer.find_index_of_columns("Max Humidity")
    date = analyzer.find_index_of_columns("PKT") 
    
    return max_temp_index, min_temp_index, mean_humidity_index, max_humidity_index, date 


def calc_month_stats( path_to_file, is_month_chart = False,):
    try:
        year_month = year_entered.split("/")
        year = year_month[0]
        month = int(year_month[1])
        if month in range(1, 13):
            if is_month_chart:
                display_monthly_chart_data(year, month, path_to_file)

            else:
                display_month_data(path_to_file, month, year)
        else:
            print("Please enter a valid month number")
            return

    except IndexError:
        if is_month_chart:
            print("Usage: python weatherman.py -c 2005/12 /path/to/files")
        else:
            print("Usage: python weatherman.py -a 2005/12 /path/to/files")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        command = sys.argv[1]
        year_entered = sys.argv[2]
        path_to_file = sys.argv[3]

        if command == "-a":
            calc_month_stats(path_to_file)
        
        elif command == "-e":
            display_year_data(year_entered[:4], path_to_file)

        elif command == "-c":
            calc_month_stats(path_to_file, is_month_chart = True)

        else:
            print("Invalid argument.")

    else:
        print("Invalid Command\nUsage: python weatherman.py -a 2005/8 /path/to/files")
