from monthly_temperature import CheckMonthlyTemperature


class MonthlyChart:
    def __init__(self, csv_array):
        self.csv_array = csv_array

    def GetResults(self, max_ind, min_ind, isSingleLine=False):
        for index in range(len(self.csv_array)):
            max_val = self.csv_array[index][max_ind]
            min_val = self.csv_array[index][min_ind]

            if isSingleLine:
                self.DisplayResultsInSingleLine(index, max_val, min_val)
            else:
                self.DisplayResults(index, max_val, min_val)

    def DisplayResults(self, index, max_val, min_val):
        if max_val != "":
            highest_temp = f"{index+1}" + " "
            for i in range(int(max_val)):
                highest_temp += "\033[31m" + "+" + "\033[0m"

        if min_val != "":
            lowest_temp = f"{index+1}" + " "
            for i in range(int(min_val)):
                lowest_temp += "\033[34m" + "+" + "\033[0m"

        highest_temp += " " + max_val + "C"
        lowest_temp += " " + min_val + "C"

        print(lowest_temp)
        print(highest_temp)

    def DisplayResultsInSingleLine(self, index, max_val, min_val):
        data_result = f"{index+1}" + " "
        if min_val != "":
            for i in range(int(min_val)):
                data_result += "\033[34m" + "+" + "\033[0m"

        if max_val != "":
            for i in range(int(max_val)):
                data_result += "\033[31m" + "+" + "\033[0m"

        data_result += " " + min_val + "C - " + max_val + "C"

        print(data_result)
