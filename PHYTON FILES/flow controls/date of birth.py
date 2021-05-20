myyear=int(input("enter your current year:"))
mymonth=int(input("enter your current month:"))
myday=int(input("enter your current day:"))
currentyear=int(input("enter the current year:"))
currentmonth=int(input("enter the current month:"))
currentday=int(input("enter the current day:"))
age=currentyear-myyear
age2=age-1

if(mymonth>=currentmonth)&(myday>=currentday):
    print("your current age is ",age2)
else:
    print("Your current age is:",age)
