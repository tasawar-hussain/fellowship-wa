import csv


class DataAnalyzer:
    def __init__(self):
        self.data_list = []
        self.column = []

    def read_file_as_csv(self, file_path):
        try:
            with open(
                file_path,
                "r",
            ) as file:
                csv_files = csv.reader(file, delimiter = ",")
                for row in csv_files:
                    if row == [] or len(row) == 1:
                        continue
                    elif any(map(lambda string: string in row[0], ('PKT', 'PKST'))):
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

    def find_index_of_columns(self, value):
        try:
            column = self.column[0]

            if value == "PKT" or value == "PKST":
                col_idx = column.index("PKT") if column.__contains__("PKT") else column.index("PKST")
            else:
                col_idx = column.index(value)
                     # max_temp_index, min_temp_index, mean_humidity_index, max_humidity_index, date
            return col_idx
        except:
            print("Header not found")
            return

        
