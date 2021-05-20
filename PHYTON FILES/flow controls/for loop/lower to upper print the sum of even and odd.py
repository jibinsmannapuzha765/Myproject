low=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))
oddsum=0
evensum=0
for i in range (low,(upper+1)):
    if (i%2==0):
        evensum+=i
        print(i)
    else:
        oddsum+=i
print(evensum)
print(oddsum)
