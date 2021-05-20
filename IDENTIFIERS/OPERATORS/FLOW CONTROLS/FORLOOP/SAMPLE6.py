# # for i in range (1,4):
# #     for j in range (1,4):
# #         print(i,end="")
# #     print("\n")
# # --------------------------------------
# # for i in range(1, 10):
# #     for j in range(1, 10):
# #         print(j, end="")
# #     print("\n")
# # -----------------------------------------
# # for i in range(1, 4):
# #     for j in range(1,(i+1)):
# #         print(j, end="")
# #     print("\n")
# # ---------------------------------------------
# # for i in range (0,5):
# #     for j in range (5-i,0,-1):
# #         print(j,end="")
# #     print()
# # ------------------------------------------------
#
# for i in range (1,6):
#     for j in range (1,(i+1)):
#         print(i,end="")
#     print()
# # --------------------------------------------
# for i in range (1,6):
#     for j in range (1,(i+1)):
#         print("*",end="")
#     print()
# # --------------------------------------------
# for i in range (1,6):
#     for j in range (6-i,0,-1):
#         print(i,end="")
#     print()
# # # --------------------------------------------
# for i in range (5,0,-1):
#     for j in range (0,i):
#         print(i,end="")
#     print()
#------------------------------------

# for i in range (6,0,-1):
#     for j in range(0,i):
#         print(j,end="")
#     print()
# -------------------------------------------
# for i in range (1,6,1):
#     for j in range (-i,0,1):
#         print(j,end=" ")
#     print()
    # ----------------------------------
#
# x=0
# for i in range (10):
#     for j in range(-1,-10,-1):
#         x+=1
#     print(x)
#    -------------------------------------

# for l in "john":
#     if l=="0":
#         pass
#     print(l,end=",")
# --------------------------------------------

# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var % 2 == 0:
#             continue
#             var += 1
#     var+=1
# else:
#     var+=1
# print(var)



x = 0
a = 5
b = 5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)









