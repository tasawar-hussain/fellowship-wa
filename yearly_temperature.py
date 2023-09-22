from datetime import datetime
from utils import YEAR_END_RESULTS


class YearWeatherAnalyzer:
    def __init__(self, weather_data_list):
        self.weather_data_list = weather_data_list
        self.year_temp_results = YEAR_END_RESULTS

    def year_analyzer( self, max_temp_index, min_temp_index, max_humid_idx, date_index, mean_humid_idx):
        for index in range(len(self.weather_data_list)):
            max_val = self.convert_data_array_values_to_integer(index, max_temp_index)
            min_val = self.convert_data_array_values_to_integer(index, min_temp_index)
            mean_humid = self.convert_data_array_values_to_integer(index, mean_humid_idx)
            max_humid = self.convert_data_array_values_to_integer(index, max_humid_idx)

            if max_val != "":
                self.calculate_highest_temp(max_val, index, date_index)
            if min_val != "":
                self.calculate_lowest_temp(min_val, index, date_index)
            if max_val != "" and mean_humid != "" :
                self.calculate_humidity(index, date_index, mean_humid, max_humid)

        return self.year_temp_results

    def calculate_highest_temp(self, max_val, index, date_index):
        if max_val >= self.year_temp_results["max_temp"]:
            self.year_temp_results["max_temp"] = max_val
            self.year_temp_results["pkt_max_temp"] = self.get_pkt_value(index, date_index)

    def calculate_humidity(
        self, index, date_index, mean_humidity,max_humidity
    ):
        if mean_humidity >= self.year_temp_results["mean_humidity"]:
            self.year_temp_results["max_humidity"] = max_humidity
            self.year_temp_results["mean_humidity"] = mean_humidity
            self.year_temp_results["pkt_humidity"] = self.get_pkt_value(index, date_index)

    def calculate_lowest_temp(self, min_val, index, date_index):
        if min_val < self.year_temp_results["min_temp"]:
            self.year_temp_results["min_temp"] = min_val
            self.year_temp_results["pkt_min_temp"] = self.get_pkt_value(index, date_index)

    def convert_data_array_values_to_integer(self, index, value_index):
        int_value = self.weather_data_list[index][value_index]
        if int_value != "":
            int_value = int(int_value)
        return int_value

    def get_pkt_value(self, index, date_index):
        value = self.weather_data_list[index][date_index]
        value = value.split("-")
        year = int(value[0])
        month = int(value[1])
        date = int(value[2])

        month_val = datetime(year, month, date).strftime("%B")

        return f"{month_val} {date}"
