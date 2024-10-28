import calendar
import datetime
leap=calendar.leapdays(2000,2080)
print(f"Number of leap years between 2000 and 2080 is: {leap}")
from datetime import datetime,timedelta
def expiary_date(issue_date):
    issue=datetime.strptime(issue_date,"%y-%m-%d")
    expiry=issue + timedelta(days=3650)
    expire_y=expiry.year
    expiry_m=expiry.month
    return expiry.date(),expire_y,expiry_m

issue_date=input("enter the passport issue date(yyyy-mm-dd): ")
expiry_date,expiry_year,expiry_month=expiary_date(issue_date)
print(f"passport expiry date{expiry_date}")
print(f"passport expiry month{expiry_month}")
print(f"passport expiry year{expiry_year}")