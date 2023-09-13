class CheckMonthlyTemperature:
    def __init__(self, csv_read_array=[]):
        self.csv_read_array = csv_read_array
        self.months_data = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]

    def MonthTemperature(self, index):
        total_entries = 0
        sum_of_entries = 0

        for i in range(len(self.csv_read_array)):
            if self.csv_read_array[i][index] != "":
                value = self.ConvertStringValues(i, index)
                sum_of_entries += value

            total_entries += 1

        average_value = round(sum_of_entries / total_entries)

        return average_value

    def CheckMonth(self, month):
        month = int(month)
        if month in range(1, 13):
            for i in range(len(self.months_data)):
                if i == month - 1:
                    return self.months_data[i]
        else:
            print("Invalid month number")

    def ConvertStringValues(self, index, value_index):
        int_value = int(self.csv_read_array[index][value_index])

        return int_value
