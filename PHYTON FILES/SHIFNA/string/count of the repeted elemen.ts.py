a=input("enter the string")
b=input("enter the element to count")
count=0
for i in a:
    if i in b:
        count+=1
print("count is",count)