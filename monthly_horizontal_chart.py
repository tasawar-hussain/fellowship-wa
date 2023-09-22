from utils  import RED_COLOR, BLUE_COLOR, BLACK_COLOR

class MonthlyWeatherVisualizer:
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.visualizer_data_result = []

    def get_results(self, max_idx, min_idx, isSingleLine=False):
        result = ""
        self.visualizer_data_result=[]

        for index in range(len(self.weather_data)):
            max_val = self.get_value_from_weather_data(index,max_idx)
            min_val = self.get_value_from_weather_data(index,min_idx)

            if isSingleLine:
                result = self.return_results_in_single_line(index, max_val, min_val)
            else:
                result = self.return_results(index, max_val, min_val)
        print(result)
    
    def get_value_from_weather_data(self, position, index_in_data):
        return self.weather_data[position][index_in_data]

    def return_results(self, position, max_val, min_val):
        data_result = self.visualizer_data_result

        if max_val != "":
            data_result.append(f"{position + 1} ")
            self.add_sign_for_max_val(max_val, data_result)
            data_result.append(f" {max_val}C \n")

        if min_val != "":
            data_result.append(f"{position + 1} ")
            self.add_sign_for_min_val(min_val, data_result)
            data_result.append(f" {min_val}C \n")

        return "".join(data_result)
        

    def return_results_in_single_line(self, position, max_val, min_val):
        data_result = self.visualizer_data_result
        data_result.append(f"\n{position + 1} ")

        if min_val != "":
            self.add_sign_for_min_val(min_val, data_result)

        if max_val != "":
            self.add_sign_for_max_val(max_val, data_result)

        data_result.append(" " + min_val + "C - " + max_val + "C")
        return "".join(data_result)

    def add_sign_for_min_val(self, value, data_result):
        for i in range(int(value)):
            data_result.append(f"{BLUE_COLOR}+{BLACK_COLOR}")

    def add_sign_for_max_val(self, value, data_result):
        for i in range(int(value)):
            data_result.append(f"{RED_COLOR}+{BLACK_COLOR}")
            
