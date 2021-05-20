num1=int(input("ENTER MARK 1"))
num2=int(input("ENTER MARK 2"))
num3=int(input("ENTER MARK 3"))
num4=int(input("ENTER MARK 4"))
total=num1+num2+num3+num4
print("TOTAL MARK",total)
if(180<=total<=200):
    print("GRADE A+")
elif(160<=total<=179):
    print("GRADE A")
elif(140<=total<=159):
    print("GRADE B+")
elif(120<=total<=139):
    print("GRADE B")
elif(100<=total<=199):
    print("GRADE C+")
elif(80<=total<=99):
    print("GRADE C")
else:
    print("GRADE D")


