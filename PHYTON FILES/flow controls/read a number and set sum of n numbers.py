# num=int(input("enter the number to find sum:"))
# i=1
# while(i<=10):
#     sum = i+num
#     print(i,"+",num,"=",sum)
#     i+=1
# =======================================================
# num=int(input("enter the number to find sum:"))
# i=1
# sum=0
# while(i<=num):
#     sum=sum+i
#     i+=1
# print(sum)
# ===========================================================
num=int(input("enter the number :"))
res=0
while(num!=0):
    dig=num%10
    res=(res*10)+dig
    num=num//10
print(res)