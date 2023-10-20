#libs 
import jdatetime
from datetime import date , datetime
import time
import pytz
import locale

iranian_months = {
    "farvardin": "فروردین",
    "ordibehesht": "اردیبهشت",
    "khordad": "خرداد",
    "tir": "تیر",
    "mordad": "مرداد",
    "shahrivar": "شهریور",
    "mehr": "مهر",
    "aban": "آبان",
    "azar": "آذر",
    "dey": "دی",
    "bahman": "بهمن",
    "esfand": "اسفند"
}



#funcs


def convert_to_persian_date(georgian_date):
    try:
        print(georgian_date)
        year, month, day = map(int, georgian_date.split('-'))
        gregorian_date = datetime.date(year, month, day)
        print(georgian_date)
        persian_date = jdatetime.date.fromgregorian(date=gregorian_date).strftime("%d %B")
        farsi=persian_date.split(' ')[0]+' '+iranian_months[(persian_date.split(' ')[1]).lower()]
        return farsi
    except AttributeError :
        return 'نامشخص' 
    except ValueError :
        return 'نامشخص'



#get current time 
def get_current_time():
    utc_time = datetime.now(pytz.utc)
    tehran_timezone = pytz.timezone('Asia/Tehran')
    tehran_time = utc_time.astimezone(tehran_timezone)
    formatted_time = tehran_time.strftime('%Y/%m/%d %H:%M:%S')
    return formatted_time



def gn():
    current_date = date.today()
    formatted_date = current_date.strftime("%Y-%m-%d")

    print(formatted_date)
    return formatted_date
