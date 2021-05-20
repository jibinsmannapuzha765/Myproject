# 4 issubclass(total mark)
#
# 180-200 a+
# 160 -179 a+
# 140-159 b
# 120-139 b+
# 100-119 c
# 80-99 c+
# 60-79 c
#
#

#   fail

mark1=int(input("ENGLISH:"))
mark2=int(input("HINDI:"))
mark3=int(input("MALAYALAM:"))
mark4=int(input("SCIENCE:"))
total=mark1+mark2+mark3+mark4
if (180<=total<=200):
    print(total)
    print(" Grade:A+")
elif (160<=total<=179):
    print(total)
    print("grade:A")
elif (140<=total<=159):
    print(total)
    print("grade:B+")
elif (120<=total<=139):
    print(total)
    print("grade:B")
elif (100<=total<=199):
    print(total)
    print("grade:C+")
elif(80<=total<=99):
    print(total)
    print("grade:C")
elif(60<=total<=79):
    print(total)
    print("grade:D+")
else:
    print(total)
    print("Fail")

