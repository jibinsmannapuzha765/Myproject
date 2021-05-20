# low=int(input("ENTER lower limit"))
# upp=int(input("ENTER upper limit"))
#
# for low in range (low,upp+1):
#      if(low%2==0):
#         print(low)


low=int(input("ENTER lower limit"))
upp=int(input("ENTER upper limit"))
oddnum=0
evennum=0
for low in range (low,upp+1):
     if(low%2==0):
        evennum=evennum+low

     if(low%2!=0):
        oddnum=oddnum+low
print(oddnum)
print(evennum)