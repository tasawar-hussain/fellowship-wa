from constants import YEAR_END_RESULTS
from utils.date_util import DateUtil


class YearWeatherAnalyzer:
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.temp_results = YEAR_END_RESULTS

    def get_year_temp_results(self, max_temp_index, min_temp_index, max_humid_idx, date_index):
        for index in range(len(self.weather_data)):
            max_val = self.convert_data_array_values_to_integer(
                index, max_temp_index)
            min_val = self.convert_data_array_values_to_integer(
                index, min_temp_index)
            max_humid = self.convert_data_array_values_to_integer(
                index, max_humid_idx)

            if max_val != "":
                self.calculate_highest_temp(max_val, index, date_index)
            if min_val != "":
                self.calculate_lowest_temp(min_val, index, date_index)
            if max_humid != "":
                self.calculate_humidity(index, date_index, max_humid)

        return self.temp_results

    def calculate_highest_temp(self, max_val, index, date_index):
        date_month = DateUtil()
        if max_val >= self.temp_results["max_temp"]:
            self.temp_results["max_temp"] = max_val
            self.temp_results["pkt_max_temp"] = date_month.get_date_month_value(
                self.weather_data[index][date_index])

    def calculate_humidity(
        self, index, date_index, max_humidity
    ):
        date_month = DateUtil()
        if max_humidity >= self.temp_results["max_humidity"]:
            self.temp_results["max_humidity"] = max_humidity
            self.temp_results["pkt_humidity"] = date_month.get_date_month_value(
                self.weather_data[index][date_index])

    def calculate_lowest_temp(self, min_val, index, date_index):
        date_month = DateUtil()
        if min_val < self.temp_results["min_temp"]:
            self.temp_results["min_temp"] = min_val
            self.temp_results["pkt_min_temp"] = date_month.get_date_month_value(
                self.weather_data[index][date_index])

    def convert_data_array_values_to_integer(self, index, value_index):
        int_value = self.weather_data[index][value_index]
        if int_value != "":
            int_value = int(int_value)
        return int_value
