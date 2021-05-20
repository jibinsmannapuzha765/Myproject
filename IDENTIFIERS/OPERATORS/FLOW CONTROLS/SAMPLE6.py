num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))

print(num1,num2,num3)
if(num2>num3>num1):
    print("the second largest number",num2)
elif(num1>num2>num3):
    print("the second largest number",num3)
else:
    print(num1)


