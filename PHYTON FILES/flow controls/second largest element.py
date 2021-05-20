num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))

print(num1,num2,num3)

if(num1>num2)&(num1>num3):
    if (num2<num3):
        print("the second largest number:",num2)
    else:
        print("the second largest element is",num3)
elif(num2>num3)&(num2>num1):
    if(num1>num2):
        print(num1)
    else:
        print(num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
      print(num1)
else:
    print(num2)
