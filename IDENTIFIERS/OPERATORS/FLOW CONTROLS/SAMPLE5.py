# salary=int(input("ENTER THE SALARY"))
# year=int(input("ENTER THE YEAR"))
# if(year>5):
#     salary=salary+(5/100)*salary
#     print("salary is",salary)
# else:
#     print("salary is",salary)


age=int(input("ENTER YOUR AGE"))
sex=input("ENTER YOUR SEX")
mar=input("ENTHER THE METERIAL STATUS")
print(age,sex,mar)

if(sex=='F'):
    print("WORK ONLY IN URBEN AREAS")
elif(sex=='M')&(age>=20)&(age<=40):
    print("work in any where")
elif(sex=='M')&(age>=40)&(age<=60):
        print("work in urben areas")
else:
    print("error")