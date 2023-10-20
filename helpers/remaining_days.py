from datetime import date
import datetime
def remaining(startdate):
   today = date.today()
   now = today.strftime("%Y-%m-%d")
   date1 = datetime.datetime.strptime(startdate, "%Y-%m-%d")
   date2 = datetime.datetime.strptime(now, "%Y-%m-%d")

   diff =  date1 - date2
   return str(diff).split(' ')[0]

def plan_date(startdate,finishdate):
   date1 = datetime.datetime.strptime(startdate, "%Y-%m-%d")
   date2 = datetime.datetime.strptime(finishdate, "%Y-%m-%d")
   diff =  date1 - date2
   return str(str(diff).split(' ')[0])


