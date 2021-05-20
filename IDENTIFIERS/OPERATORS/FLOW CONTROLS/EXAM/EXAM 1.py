



# def Remove(dup):
#     list=[]
#     for num in dup:
#         if num not in list:
#             list.append(num)
#     return list
# dup=[2,4,10,20,5,2,20,4]
# print(Remove(dup))





def triangle(n):
    k=n-1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*", end="")
        print("\r")
n=5
triangle(n)




# num=int(input("Enter a number:"))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number is palindrome")
# else:
#     print("Not a palindrome")




#  for i in range (0,6):
#      for j in range (0,i+1):
#     print("*",end="")
# print()
















