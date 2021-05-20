
#x="[abc]"      either a b or c
# import re
# x="[abc]"
# matcher=re.finditer(x,"aldsaihfciuwdbhf")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# exept abc
# import re
#
# x="[^abc]"
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# a to z
# import re
#
# x="[a-z]"
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# A to Z
# import re
#
# x="[A-Z]"
# matcher=re.finditer(x,"abt c@5Akz")
# for match in matcher:
#     print(match.group())
#     print(match.start(),end=" ")


# both lower and upper cases are checked
# import re
#
# x="[a-zA-Z]"
# matcher=re.finditer(x,"abt c@5Akz")
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())

# check the degites
# import re
#
# x="[0-9]"
# matcher=re.finditer(x,"abt c@5Akz")
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())




# special sympols
# import re
#
# x="[^a-zA-Z0-9]"
# matcher=re.finditer(x,"abt c@5Akz")
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())


#check the space
# import re
#
# x='\s'
# matcher=re.finditer(x,"abt c@5Akz")
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())


# check the digits
# import re
# x='\d'
# matcher=re.finditer(x,"abt c@5Akz")
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())

# execpt digits
# import re
# x='\D'
# matcher=re.finditer(x,"abt c@5Akz")
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())


# all words asnd numbers execpt the special charatris
# import re
# x='\w'
# matcher=re.finditer(x,"abt c@5Akz")
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())



# for special chariters
# import re
# x='\W'
# matcher=re.finditer(x,"abtc@5Akz")
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())





# ---------------------------------------------------------------------------------------
# quantifiers
# ---------------------------------------------------------------------------------------

# a including group
# import re
# x='a+'
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,"abt c@5Akz")
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())
# --------------------------------------------------------------------------------------
# count including 0 number of a
# import re
# x="a*"
# r="aaa abc aaaa aa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())
# -----------------------------------------------------------------------------------
# count a as each including 0 no of a
# import re
# x='a?'
# r="aaa abc aaaa caga"
# matcher=re.finditer(x,"abt c@5Akz")
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())

# ------------------------------------------------------------------------------------------
# number of 2a
# import re
# x="a{2}"
# r="aaa abc aaaa caga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())

# ==================================================
# minimum 2a and maximum 3 a
# import re
# x="a{2,3}"
# r="aaa abc aaaa aa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())

# ---------------------------------------------------
# check starting with a
# import re
# x="^a"
# r="aaa abc aaaa aa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())

# -----------------------------------------------------
#     check ending with a
# import re
# x="a$"
# r="aaa abc aaaa aa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),end=" ")
#     print(match.group())




