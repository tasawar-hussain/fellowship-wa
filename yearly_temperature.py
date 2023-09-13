from datetime import datetime


class YearlyTemperature:
    def __init__(self, csv_read_array):
        self.csv_read_array = csv_read_array
        self.year_temp_results = {
            "max_temp": 0,
            "pkt_max_temp": "",
            "min_temp": 0,
            "pkt_min_temp": "",
            "max_humidity": 0,
            "min_humidity": 0,
            "mean_humidity": 0,
            "pkt_humidity": "",
        }

    def YearTemperature(
        self,
        max_temp_index,
        min_temp_index,
        max_humidity_index,
        date_index,
        mean_hum_ind,
        min_hum_ind,
    ):
        self.year_temp_results["min_temp"] = self.ConvertStringValues(0, min_temp_index)

        for index in range(len(self.csv_read_array)):
            max_val = self.ConvertStringValues(index, max_temp_index)
            min_val = self.ConvertStringValues(index, min_temp_index)
            max_humd = self.ConvertStringValues(index, max_humidity_index)
            mean_humd = self.ConvertStringValues(index, mean_hum_ind)
            min_hum = self.ConvertStringValues(index, min_hum_ind)

            if max_val != "":
                self.CalculateHighestTemp(max_val, index, date_index)
            if min_val != "":
                self.CalculateLowestTemp(min_val, index, date_index)

            if max_val != "" and mean_humd != "" and min_hum != "":
                self.CalculateMaximumHumidty(
                    max_humd, index, date_index, mean_humd, min_hum
                )

        return self.year_temp_results

    def CalculateHighestTemp(self, max_val, index, date_index):
        if max_val >= int(self.year_temp_results["max_temp"]):
            self.year_temp_results["max_temp"] = max_val
            self.year_temp_results["pkt_max_temp"] = self.GetPktDate(index, date_index)

    def CalculateMaximumHumidty(
        self, max_humidity, index, date_index, mean_hum, min_hum
    ):
        if max_humidity >= self.year_temp_results["max_humidity"]:
            self.year_temp_results["max_humidity"] = max_humidity
            self.year_temp_results["min_humidity"] = mean_hum
            self.year_temp_results["mean_humidity"] = min_hum
            self.year_temp_results["pkt_humidity"] = self.GetPktDate(index, date_index)

    def CalculateLowestTemp(self, min_val, index, date_index):
        if min_val < self.year_temp_results["min_temp"]:
            self.year_temp_results["min_temp"] = min_val
            self.year_temp_results["pkt_min_temp"] = self.GetPktDate(index, date_index)

    def ConvertStringValues(self, index, value_index):
        int_value = self.csv_read_array[index][value_index]

        if int_value != "":
            int_value = int(int_value)

        return int_value

    def GetPktDate(self, index, date_index):
        value = self.csv_read_array[index][date_index]
        value = value.split("-")
        year = int(value[0])
        month = int(value[1])
        date = int(value[2])

        month_val = datetime(year, month, date).strftime("%B")

        return f"{month_val} {date}"
