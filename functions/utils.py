from datetime import date
from dateutil.relativedelta import *

class DateUtils():
    def format(date):
        if (date):
           return date.strftime("%d/%m/%y")
        else:
           return None
       
    def age_years(date):
        if (not date):
           return None
        today = date.today()
        if (today.month >= date.month):
           return today.year - date.year
        else:
           return today.year - date.year - 1
       
    def age_months(date):
        if (not date):
            return None
        today = date.today()
        if (today.month == date.month):
            return 0
        elif (today.month > date.month):
            if (today.day >= date.day):
                return today.month - date.month
            else:
                return today.month - date.month -1
        else:
            if (today.day >= date.day):
                return today.month + (12-date.month)
            else:
                return today.month + (12-date.month)-1
       
    #incrementa days dias à data date
    def future_days(date, days):
        if (date):
          return date.fromordinal(date.toordinal()+days)
        else:
          return None
      
    #incrementa months meses a data date
    def future_months(date, months):
        return date+relativedelta(months=+months)
        