import sys
from weather_report import WeeklyReport

if __name__ == "__main__":
    if len(sys.argv) == 4:
        command = sys.argv[1]
        year_entered = sys.argv[2]
        path_to_file = sys.argv[3]
        report = WeeklyReport(path_to_file, year_entered)

        if command == "-a":
            report.calc_month_stats(year_entered)

        elif command == "-e":
            report.display_year_data(year_entered[:4])

        elif command == "-c":
            report.calc_month_stats(year_entered, is_month_chart=True)

        else:
            print("Invalid argument.")

    else:
        print("Invalid Command\nUsage: python weatherman.py -a 2005/8 /path/to/files")
