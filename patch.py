import datetime
today=datetime.datetime.now()
print("Today : "+str(today))
month=today.month
year=today.year
print("current Month and year is:"+str(month)+" "+str(year))
first_day=datetime.datetime(year,month, 1)
print(first_day)
print("Calculating Monday, Wednesday, Friday of the corresponding week in which 3rd saturday falls")
day_num=first_day.strftime("%w")
print(day_num)
#calculating the first Saturday's date of the month
first_sat_date=7-int(day_num)
#calculating the third saturday's date of the month
third_sat_date=first_sat_date+14
#monday,wednesday,friday dates of the corresponding week in which 3rd saturday falls.
mon,wed,thu=third_sat_date-5,third_sat_date-3,third_sat_date-2
print(mon,wed,thu)
d=today.day
