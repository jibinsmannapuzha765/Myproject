# def shuffle_values(func):
#     def wrapper(no1,no2):
#         if(no1>no2):
#             (no1,no2)=(no2,no1)
#         return func(no1,no2)
#     return wrapper
#
# @shuffle_values
# def div(num1,num2):
#     return num1/num2
# @shuffle_values
# def subtract(no1,no2):
#     return no1-no2
# print(div(2,10))
# print(subtract(8,10))
# --------------------------------------------------------


def change_pin(user,pin):
    mypin=pin
    return mypin

def delete_account(user,acno):
    return str(acno+"deleted")


