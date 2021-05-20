def fact():
    num=int(input("enter the number:"))
    fac=1
    for i in range(1,num+1):
         fac*=i
    print(fac)
fact()