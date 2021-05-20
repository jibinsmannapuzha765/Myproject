a=input("enter the string")
count=0
for i in a:
    if i in "aeiou":
        count+=1
    else:
        pass
print("count is vowels",count)