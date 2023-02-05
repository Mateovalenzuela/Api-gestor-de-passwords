import datetime


class DateFormat:

    @classmethod
    def convert_date(cls, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')
