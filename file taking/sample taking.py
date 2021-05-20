# f = open("D:\customer.doc", "r")
# for lines in f:
#     data = lines.rstrip("/n").split(",")
#     fname = data[1]
#     age = data[3]
#     cou = data[-1]
#     lst = ([fname, age, cou])
#     for i in lst:
#           if (lst[2] == "india"):
#            print(lst)




 # print(fname,",",age,",",cou)

# f = open("D:\customer.doc", "r")
# dic={}
# for lines in f:
#     word=lines.rstrip("\n").split(",")
#     prof=word[4]
#     if prof not in dic:
#         dic[prof]=1
#     else:
#         dic[prof]+=1
# print(dic)
#
# f = open("D:\customer.doc", "r")
# dic={}
# for lines in f:
#     word = lines.rstrip("\n").split(",")
#     data1 = word[4]

f=open("D:\Temperature.doc", "r")
dic = {}
for lines in f:
    word = lines.rstrip("\n").split(",")
    print(word)
        # data1 = word[4]