from constants import COLORS, TEMP_SYMBOL


class MonthlyBarChart:
    def __init__(self, weather_data):
        self.weather_data = weather_data

    def print_bar_results(self, max_idx, min_idx, isSingleLine=False):
        result = ""
        data_result = []

        for index in range(len(self.weather_data)):
            max_val = self.get_value_from_weather_data(index, max_idx)
            min_val = self.get_value_from_weather_data(index, min_idx)

            if isSingleLine:
                result = self.get_results_in_single_line(
                    index, max_val, min_val, data_result)
            else:
                result = self.get_chart_results(
                    index, max_val, min_val, data_result)
        print(result)

    def get_value_from_weather_data(self, position, index_in_data):
        return self.weather_data[position][index_in_data]

    @classmethod
    def get_chart_results(cls, position, max_val, min_val, data_result):
        if min_val != "":
            data_result.append(f"{position + 1} ")
            string = cls.colored_string(COLORS['BLUE'], TEMP_SYMBOL, min_val)
            data_result.append(f"{string} {min_val}C \n")

        if max_val != "":
            data_result.append(f"{position + 1} ")
            string = cls.colored_string(COLORS['RED'], TEMP_SYMBOL, max_val)
            data_result.append(f"{string} {max_val}C \n")

        return "".join(data_result)

    @classmethod
    def get_results_in_single_line(cls, position, max_val, min_val, data_result):
        if min_val != "" and max_val != "":
            data_result.append(f"\n{position + 1} ")
            string = cls.colored_string(COLORS['BLUE'], TEMP_SYMBOL, min_val)
            data_result.append(string)
            string = cls.colored_string(COLORS['RED'], TEMP_SYMBOL, max_val)
            data_result.append(string)

            data_result.append(" " + min_val + "C - " + max_val + "C")

        return "".join(data_result)

    @classmethod
    def colored_string(cls, color, string, times):
        return f"{color}{string*int(times)}{COLORS['BLACK']}"
