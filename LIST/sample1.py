list=[2,4,7,8,7,10]
element=int(input("enter the element to be search:"))
flag=0
for i in list:
    if(i==element):
        flag=1
        break
    else:
        pass
    if(flag>0):
        print("element found")
    else:
        print("element not found")
