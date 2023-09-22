from utils import MONTHS


class MonthlyWeatherAnalyzer:
    def __init__(self, weather_data_list = []):
        self.weather_data_list = weather_data_list
        self.months_data = MONTHS

    def calculate_average_value(self, position):
        total_entries = 0
        sum_of_entries = 0
        data_list = self.weather_data_list

        for i in range(len(data_list)):
            if data_list[i][position] != "":
                value = self.data_array_convert_string_values_to_integer(i, position)
                sum_of_entries += value

            total_entries += 1

        average_value = round(sum_of_entries / total_entries)

        return average_value

    def get_month_value(self, month):
        month = int(month)
        if month in range(1, 13):
            return self.months_data[month]
        else:
            print("Invalid month number")

    def data_array_convert_string_values_to_integer(self, index, value_index):
        try:
            int_value = int(self.weather_data_list[index][value_index])

            return int_value
        except IndexError:
            print("Index out of bound")
            return
