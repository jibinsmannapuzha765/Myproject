# num=int(input("ENTER THE NUMBER"))
# if (num%2==0):
#     print("the number is even")
# else:
#     print("the number is odd")
# -----------------------------------------------------
# num1=int(input("enter the first num"))
# num2=int(input("enter the 2nd num"))
#
# if (num1>=num2):
#     print("higher")
# else:
#     print(num2)
# --------------------------------------------------------------------

# num=int(input("ENTER THE NUMBER"))
# if (num>0):
#     print("the number is positive")
# elif(num==0):
#     print("the number is equal")
# else:
#     print("the number is negitive")
    # =================================================================

# num1=int(input("ENTER THE 1ST NUMBER"))
# num2=int(input("ENTER THE 2ND NUMBER"))
# if (num1>num2):
#     print("the number is positive")
# elif(num1==num2):
#     print("the number is equal")
# else:
#     print("the number is negitive")
# ---------------------------------------------------------

num1=int(input("ENTER THE 1ST NUMBER"))
num2=int(input("ENTER THE 2ND NUMBER"))
num3=int(input("ENTER THE THIRD NUMBER"))
if (num1>num2)&(num1>num3):
    print("the number is maximum",num1)
elif(num2>num1)&(num2>num3):
    print("the number is maximum",num2)
else:
    print("the number is maximum",num3)