from constants import CITY_NAME as CITY
from constants import WEATHER_FILE_HEADERS

from data_reader import DataReader
from monthly_horizontal_chart import MonthlyBarChart
from monthly_temperature import MonthlyWeatherAnalyzer

from utils.date_util import DateUtil
from utils.file_util import FileUtil
from yearly_temperature import YearWeatherAnalyzer


class WeeklyReport:
    def __init__(self, file_path, year_entered):
        self.file_path = file_path
        self.year_entered = year_entered

    def display_year_data(self, year):
        try:
            months_file_list = FileUtil.files_for_given_year(
                self.file_path, year)

            for file in months_file_list:
                reader = DataReader()
                data_list = reader.read_file_as_csv(file)

                max_temp_index = reader.find_index_of_header_name(
                    WEATHER_FILE_HEADERS["MaxTemperatureC"])
                min_temp_index = reader.find_index_of_header_name(
                    WEATHER_FILE_HEADERS["MinTemperatureC"])
                max_humidity_index = reader.find_index_of_header_name(
                    WEATHER_FILE_HEADERS["MaxHumidity"])
                date = reader.find_index_of_header_name(
                    WEATHER_FILE_HEADERS["Date"])

                analyzer = YearWeatherAnalyzer(data_list)
                data_dict = analyzer.get_year_temp_results(
                    max_temp_index, min_temp_index, max_humidity_index, date, )

            print(
                f"Highest: {data_dict['max_temp']}C on {data_dict['pkt_max_temp']}")
            print(
                f"Lowest: {data_dict['min_temp']}C on {data_dict['pkt_min_temp']}")
            print(
                f"Humid: {data_dict['max_humidity']}% on { data_dict['pkt_humidity']}")

        except FileNotFoundError:
            print(f"File with {year} doesn't exist")
            return

    def display_month_results(self, month, year):
        month = DateUtil.get_month_name(month)
        file_path = f"{self.file_path}/{CITY}_weather_{year}_{month}.txt"

        reader = DataReader()
        data_list = reader.read_file_as_csv(file_path)
        max_temp_index = reader.find_index_of_header_name(
            WEATHER_FILE_HEADERS["MaxTemperatureC"])
        min_temp_index = reader.find_index_of_header_name(
            WEATHER_FILE_HEADERS["MinTemperatureC"])
        mean_humidity_index = reader.find_index_of_header_name(
            WEATHER_FILE_HEADERS["MeanHumidity"])

        monthly_temp = MonthlyWeatherAnalyzer(data_list)
        highest_average = monthly_temp.calculate_average_value(
            max_temp_index)
        lowest_average = monthly_temp.calculate_average_value(
            min_temp_index)
        average_humidity = monthly_temp.calculate_average_value(
            mean_humidity_index)

        print(f"Highest Average: {highest_average}C")
        print(f"Lowest Average: {lowest_average}C")
        print(f"Average Humidity: {average_humidity}%")

    def display_monthly_chart_result(self, year, month):
        month = DateUtil.get_month_name(month)
        try:
            file_path = f"{self.file_path}/{CITY}_weather_{year}_{month}.txt"

            reader = DataReader()
            data_list = reader.read_file_as_csv(file_path)
            max_temp_index = reader.find_index_of_header_name(
                WEATHER_FILE_HEADERS["MaxTemperatureC"])
            min_temp_index = reader.find_index_of_header_name(
                WEATHER_FILE_HEADERS["MinTemperatureC"])

            print(f"\n{month} {year}")
            monthly_chart = MonthlyBarChart(data_list)
            monthly_chart.print_bar_results(max_temp_index, min_temp_index)

            print(f"\nBonus Task\n{month} {year}")
            monthly_chart.print_bar_results(
                max_temp_index, min_temp_index, True)
        except:
            print("An error occured while reading file")

    def calc_month_stats(self, year_entered, is_month_chart=False):
        try:
            year_month = year_entered.split("/")
            year = year_month[0]
            month = int(year_month[1])
            if month in range(1, 13):
                if is_month_chart:
                    self.display_monthly_chart_result(year, month)
                else:
                    self.display_month_results(month, year)
            else:
                print("Please enter a valid month number")
                return

        except IndexError:
            if is_month_chart:
                print("Usage: python weatherman.py -c 2005/12 /path/to/files")
            else:
                print("Usage: python weatherman.py -a 2005/12 /path/to/files")
