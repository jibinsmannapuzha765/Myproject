# import re
#
# n= "hello2"
# x='\w*'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("valid")

# import re
#
# n= "57kg jyg25fggSD@"
# x="\w*"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# import re
#
# n=input("enter the mob num")
# x='\d{10}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

import re

n=input("enter the mob num")
x="\W\d{12}"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
