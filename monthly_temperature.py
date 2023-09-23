class MonthlyWeatherAnalyzer:
    def __init__(self, weather_data=[]):
        self.weather_data = weather_data

    def calculate_average_value(self, position):
        total_entries = 0
        sum_of_entries = 0
        data_list = self.weather_data

        for i in range(len(data_list)):
            if data_list[i][position] != "":
                value = self.data_array_convert_string_values_to_integer(
                    i, position)
                sum_of_entries += value

            total_entries += 1

        average_value = round(sum_of_entries / total_entries)

        return average_value

    def data_array_convert_string_values_to_integer(self, index, value_index):
        try:
            int_value = int(self.weather_data[index][value_index])

            return int_value
        except IndexError:
            print("Index out of bound")
            return
