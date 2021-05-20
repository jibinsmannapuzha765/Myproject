# class Person:
#     def setval(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def print(self):
#         print(self.name,self.age,self.sex)
#
# pe=Person("anu",26,"fem")
# pe.print()


# class Emp:
#     def __init__(self, name, age,place, sex,position):
#         self.name = name
#         self.age = age
#         self.place=place
#         self.sex = sex
#         self.position=position
#
#     def print(self):
#         print(self.name, self.age,self.place, self.sex,self.position)
#
#
# pe.print()
#
# pe = Emp("soman", 36,"pathanamthitta","male","IT MANAGER")


# class Person:
#     def details(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def printdata(self):
#             print(self.name)
#             print(self.age)
#             print(self.sex)
# class Student(Person):
#     def det(self,num,school):
#         self.num=num
#         self.school=school
#     def prints(self):
#         print(self.num)
#         print(self.school)
# per=Person()
# per.details("anu",23,"fem")
# per.printdata()
# st=Student()
# st.det(25,"mount")
# st.prints()

class Employee:
    def details(self,name,id):
        self.name=name
        self.id=id
    def __str__(self):
        return self.name+str(self.id)
a=Employee()
a.details("jibin",2569)
print(a)


