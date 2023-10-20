import datetime
import jdatetime
import sys
import os 
sys.path.append(str(os.getcwd().replace('\\','/')))
from handle_configs import get_extra

def convert_to_persian_date(georgian_date):
    try:
        # print(georgian_date)
        year, month, day = map(int, georgian_date.split('-'))
        gregorian_date = datetime.date(year, month, day)
        # print(georgian_date)
        persian_date = jdatetime.date.fromgregorian(date=gregorian_date).strftime("%d %B")
        farsi=persian_date.split(' ')[0]+' '+get_extra(persian_date.split(' ')[1].lower())
        return farsi
    except AttributeError :
        return 
    except ValueError :
        return 'نامشخص'

