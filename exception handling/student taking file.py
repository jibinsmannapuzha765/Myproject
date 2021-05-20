# class Student:
#     def details(self,name,age):
#         self.name=name
#         self.age=age
#     def printval(self):
#         print(self.name,self.age)
# f=open("Student","r")
# pp=Student()
#
# for i in f:
#     data=i.rstrip("\n").split(",")
#     pp.details(data[0],data[1])
#     pp.printval()

# class Student:
#     def details(self,name,roll,dept,mark):
#         self.name=name
#         self.roll=roll
#         self.dept=dept
#         self.mark=mark
#     def printval(self):
#         print(self.name,self.roll,self.dept,self.mark)
#
# f=open("Student","r")
#
# for i in f:
#     data=i.rstrip("\n").split(",")
#
#     obj=Student()
#     obj.details(data[0],data[1],data[2],data[3])
#     if int(data[3]) > 190:
#         obj.printval()
# -------------------------------------------------------------------------
# overloading
# ---------------------------------------------------------------------------

# class Student:
#     def details(self,name,roll,dept,mark):
#         self.name=name
#         self.roll=roll
#         self.dept=dept
#         self.mark=mark
# class Child(Student):
#     def set(self,sname,sage):
#         self.sname=sname
#         self.sage=sage
#
#         print(self.sname,self.sage)
# ch=Child()
# ch.set("jdfgjkgf",98,"cs",98)
# ---------------------------------------------------------------------------------------------

# class Parent:
#     def properties(self):
#         print("10 lak rupee")
# class Marry:
#     def marry(self):
#         print("with arun")
# class Child(Parent):
#     def marry(self):
#      print("with ram")
#
# c=Child()
# c.marry()
# # ---------------------------------------------------------------------------------
#
# class Parent:
#     def properties(self,name,sex):
#         self.name=name
#         self.sex=sex
#         print(self.name,self.sex)
# class Student:
#     def marry(self,dept,roll):
#         self.dept=dept
#         self.roll=roll
#         print(self.dept,self.roll)
# class Child(Parent):
#     def marry(self,name,sex):
#         self.name=name
#         self.sex=sex
#      print()
# c.Marry()
# c=Child()
# --------------------------------------------------------------------------------
