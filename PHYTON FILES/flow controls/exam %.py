class1=int(input("Total Class:"))
class2=int(input("Total Classes Attented:"))
avg=(class2/class1)*100
print("Total Average of Attentence:",avg,"%")
if (avg>=75):
    print("Student Can Attent The Exam")
else:
    print("St\udent Can't Attent The Exam")