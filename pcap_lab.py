from datetime import datetime

# 2020/11/04 14:53:00
# 20/November/04 14:53:00 PM
# Wed, 2020 Nov 04
# Wednesday, 2020 November 04
# Weekday: 3
# Day of the year: 309
# Week number of the year: 44


date = datetime(2020, 11, 4, 14, 53)
print(datetime.strftime(date, "%Y/%m/%d %H:%M:%S"))
print(datetime.strftime(date, "%y/%B/%d %H:%M:%S %p"))
print(datetime.strftime(date, "%a, %Y %b %d"))