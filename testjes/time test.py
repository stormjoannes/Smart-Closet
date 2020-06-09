from datetime import datetime

# today = date.today()
# print(today)
# print(today + 1)
#
#
# today = str(today)
# today = today.split("-")
# print(today[2])
#
# date1 = "2020-06-09"
# date2 = "2020-06-12"
# diffrence = delta.day

# from datetime import datetime
# date_format = "%m/%d/%Y"
# a = datetime.strptime('8/18/2008', date_format)
# b = datetime.strptime('9/26/2008', date_format)
# delta = b - a
# print(delta.days)

# today = datetime.date.today()
# tussen = str(today)







today = datetime.today()
date_format = "%Y-%m-%d"
tja = today

print(tja)

tja2 = datetime.strptime('2020-06-11', date_format)
print(tja2)

diff = tja - tja2
print(abs(diff.days))


# someday = datetime.date(2008, 12, 25)
# diff = someday - today
# print(abs(diff.days))



#
# today = datetime.today()
# today = today.split('-')

