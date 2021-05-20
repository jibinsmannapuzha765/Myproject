def add(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
print("1.ADD")
print("2.SUBTRACTION")
print("3.MULTIPLY")
print("4.DIVISION")
while True:
    choice=input("Enter your choice")
    if choice in ('1','2','3','4'):
        num1=float(input("Enter a number"))
        num2=float(input("Enter a number"))
        if choice=='1':
            print(add(num1,num2))
        elif choice=='2':
            print(subtraction(num1,num2))
        elif choice=='3':
            print(multiply(num1,num2))
        elif choice=='4':
            print(division(num1,num2))
        break
    print("invalied")
