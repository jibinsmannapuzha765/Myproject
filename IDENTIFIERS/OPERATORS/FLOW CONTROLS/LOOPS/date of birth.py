year=int(input("ENTER THE CURRENT YEAR:""\n"))
month=int(input("ENTER THE CURRENT MONTH:""\n"))
day=int(input("ENTER THE CURRENT DAY:""\n"))
myyear=int(input("ENTER YOUR YEAR:""\n"))
mymonth=int(input("ENTER YOUR MONTH:""\n"))
myday=int(input("ENTER YOUR DAY:""\n"))
sum=(year-myyear)
if(month<mymonth):
    print("ERROR:""\n")
elif(year>myyear):
    print("ERROR:""\n")
else:
    print("YOUR CURRENT AGE IS:""\n",sum)







# from datetime import date
# def calculate_age(dtob):
#     today=date.today()
#     return today.year-dtob.year-((today.month,today.day)<(dtob.month,dtob.day))
# print()
# print(calculate_age(date(2022,10,30)))
# print(calculate_age(date(1989,10,30)))
# print()
