import locale
from datetime import date
from dateutil.relativedelta import *

class DateUtils():
    def format(date):
        if (date):
           return date.strftime("%d/%m/%y")
        else:
           return None
       
    def age_years(start_date, end_date = date.today()):
        if (not start_date):
           return None

        if (end_date.month >= start_date.month):
           return end_date.year - start_date.year
        else:
           return end_date.year - start_date.year - 1
       
    def age_months(start_date, end_date = date.today()):
        if (not start_date):
            return None
        if (end_date.month == start_date.month):
            return 0
        elif (end_date.month > start_date.month):
            if (end_date.day >= start_date.day):
                return end_date.month - start_date.month
            else:
                return end_date.month - start_date.month -1
        else:
            if (end_date.day >= start_date.day):
                return end_date.month + (12-start_date.month)
            else:
                return end_date.month + (12-start_date.month)-1
       
    #incrementa days dias à data date
    def future_days(date, days):
        if (date):
          return date.fromordinal(date.toordinal()+days)
        else:
          return None
      
    #incrementa months meses a data date
    def future_months(date, months):
        return date+relativedelta(months=+months)
        
class CurrencyUtils():
    def format(value):
        if (value):
            locale.setlocale(locale.LC_ALL, '' )
            return locale.currency(value)
        else:
            return None;
