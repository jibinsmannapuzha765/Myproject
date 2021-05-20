num1=10
num2=20
temp3=num1
num1=num2
num2=temp3


print(num1)
print(num2)

print("after swapping")

print(num1)
print(num2)

print("using operators")
(num1,num2)=(num2,num1)
print(num1,num2)

print("using operators")
num1=num1+num2        #10=10+20=30
num2=num1-num2        #20=30-20=
num1=num1-num2

print(num1)
print(num2)


