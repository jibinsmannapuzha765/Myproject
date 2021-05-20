# def add(*arg):
#     result =0
#     for num in arg:
#         result+=num
#     return result
# print


# cube=lambda num:num**3
# print(cube(3))

# fst=lambda word:word[0]
# print(fst("good morng"))

# map

# lst=[2,3,4,5,6]
# sq=[]
# for num in list:
#     res=num%2
#     sq.append(res)
# lst

# lst=[2,3,4,5,6]
# def sq(num):
#     return num*2
# sq=list(map(sq,lst))
# print(sq)
# -------------------------------------
# lst=[2,3,4,5,6]
# sq=list(map(lambda num:num**2,lst))
# print(sq)


# names=["jibin","badu","jain"]
# def to_upper(name):
#     return name.upper()
# upp=list(map(to_upper,names))
# print(upp)

# names=["jibin","badu","jain"]
# upp=(list((map(lambda name:name.upper(),names))
# print(upp)


# num1=10
# num2=20
# large=num1 if num1>num2 else num2
# print(large)


lst=[7,8,9,4,3,2]
op=list(map(lambda num:num+1 if num>5 else num-1,lst))
print(op)

