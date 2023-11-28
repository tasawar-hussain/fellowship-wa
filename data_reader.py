import csv
from constants import WEATHER_FILE_HEADERS


class DataReader:
    def __init__(self):
        self.data_list = []
        self.column = []

    def read_file_as_csv(self, file_path):
        try:
            with open(
                file_path,
                "r",
            ) as file:
                csv_files = csv.reader(file, delimiter=",")
                for row in csv_files:
                    if row == [] or len(row) == 1:
                        continue
                    elif any(map(lambda string: string in row[0], (WEATHER_FILE_HEADERS["Date"], WEATHER_FILE_HEADERS["Date_S"]))):
                        self.column.append(row)
                    else:
                        self.data_list.append(row)

                return self.data_list

        except FileNotFoundError:
            print("Unable to locate file. Make sure that the path is correct")
            return
        except:
            print("Error occured while reading file")
            return

    def find_index_of_header_name(self, value):
        try:
            column = self.column[0]

            if value == (WEATHER_FILE_HEADERS["Date"] or WEATHER_FILE_HEADERS["Date_S"]):
                col_idx = self.get_date_index(column)
            else:
                col_idx = column.index(value)
            return col_idx
        except:
            print("Header not found")
            return

    @classmethod
    def get_date_index(cls, column):
        if WEATHER_FILE_HEADERS['Date'] in column:
            return column.index(WEATHER_FILE_HEADERS["Date"])
        else:
            return column.index(WEATHER_FILE_HEADERS["Date_S"])
