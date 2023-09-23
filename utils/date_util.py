from datetime import datetime


class DateUtil:
    @staticmethod
    def get_date_month_value(value):
        date_time = datetime.strptime(value, "%Y-%m-%d")
        date = date_time.day
        month_val = date_time.strftime("%B")

        return f"{month_val} {date}"

    @staticmethod
    def get_month_name(value):
        date_time = datetime.strptime(str(value), "%m")
        month_name = date_time.strftime("%b")

        return month_name
