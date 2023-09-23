import os


class FileUtil:
    @staticmethod
    def files_for_given_year(path, year):
        list = []
        for file in os.listdir(path):
            if file.__contains__(year):
                file_path = f"{path}/{file}"
                list.append(file_path)

        return list
