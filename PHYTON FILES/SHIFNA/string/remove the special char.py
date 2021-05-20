punch="!@#$%^&*()_+:?><"
my_str=input("enter the string")
no_punch=""
for char in my_str:
    if char not in punch:
        no_punch=no_punch+char
