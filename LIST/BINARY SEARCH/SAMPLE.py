# binary search

# list=[2,4,7,1,5]
#
# 1> sort the given array
#
# list=[1,2,4,5,7]
#     low       upp
# 2>low=0
#
# upper=len(list)-1
#
# 3>mid
#
# mid=low+upper//2
#
# >have 3 contations should be apply
#
# 1. low=mid+1
# 2 upper=mid-1
# 3 element=list(mid)
# ----------------------------------------------------------
# mid=(low+upp)//2




# list=[1,2,4,5,7]
# list.sort()
# low=0
# upper=len(list)-1
# flag=0
# element=int(input("enter the element:"))
# while(low<=upper):
#     mid=(low+upper)//2
#     if(element>list[mid])
#         low=mid+1
#     elif(element<list[mid]):
#         low=mid-1
#     elif(element==list[mid]):
#         flag=1
#
#
# if (flag>0):
#     print("element found")
# else:
#     print("element found")
# -------------------------------------------------------------


# list=[1,5,3,7,9]
# element=int(input("enter the element"))
# k=12
# res[]
# for i in list:
#     y=k-i
#     if (i!=y and list[y]) or (i==y and list[y]>1):
#         res.append((x,y))


def element(lst,K):
    res = []
    while lst:
        num=lst.pop()
        diff=K-num
        if diff in lst:
            res.append((diff,num))
    res.reverse()
    return res
lst=[1,5,3,7,9]
K=12
print(element(lst,K))






# elif(search>list[mid]):
#     upper=mid-1
# elif(search==list[mid]):
#     print("found")







