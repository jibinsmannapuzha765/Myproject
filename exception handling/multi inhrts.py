# class Parent:
#     def m1(self):
#      print("inside parent")
# class Child:
#     def m2(self):
#      print("inside child class")
# class Subchild(Child,Parent):
#     def m3(self):
#      print("inside subchild")
# obj=Subchild()
# obj.m3()
# obj.m2()
# obj.m1()

# class School:
#     def m1(self):
#      print("MOUNT")
# class Student:
#     def m2(self):
#      print("Jibin")
# class std(Student,School):
#     def m3(self):
#      print(7)
# obj=std()
# obj.m3()
# obj.m2()
# obj.m1()



# class School:
#     def sl(self,school):
#     self.school=school
#     def printsl(self.school):
#
# class Student(School):
#     def st(self,name):
#     self.name=name
#     def printna(self.name):
#
# class Std(Student):
#     def sd(self,std):
#     self.std=std
#     def printsd(self.std)
# obj=Std()
# obj.sd(7)
# obj.st("jibin")
# obj.sl("mount")


# ------------------------------------------------------------------
# class Parent:
#     def m1(self):
#      print("inside parent")
# class Child(Parent):
#     def m2(self):
#      print("inside child class")
# class Subchild(Child):
#     def m3(self):
#      print("inside subchild")
# obj=Subchild()
# obj.m3()
# obj.m2()
# obj.m1()
# obj2=Child()
# obj2.m2()
# obj2.m1()
# --------------------------------------------------------------------------
# class College:
#     def m1(self):
#      print("Collage Name:")
#
# class Student:
#     def m2(self):
#      print("Student Name:")
#
# class Sub(Student,College):
#     def m3(self):
#      print("Subject Name:")
#
# obj=Sub()
# obj.m3("Science")
# obj.m2("Jibin")
# obj.m1("Mount")
# obj2=Student()
# obj2.m2("Jibin")
# obj2.m1("Mount")
# -------------------------------------------------------

# class Person:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def printval1(self):
#         print(self.name)
#         print(self.age)
#         print(self.sex)
# class Parent(Person):
#     def __init__(self,location,desig,exp):
#         super().__init__(name,age,sex)
#         self.location=location
#         self.desig=desig
#         self.exp=exp
#     def printval2(self):
#         print(self.location)
#         print(self.desig)
#         print(self.exp)
# class Child(Person):
#     def __init__(self,dob):
#         self.dob=dob
#         print(self.dob)
# class Student(Child):
#     def __init__(self,name,roll,mark):
#         self.name=name
#         self.roll=roll
#         self.mark=mark
#         print(self.name)
#         print(self.roll)
#         print(self.mark)
#
# cc=Parent("jibin","pathanamthitta","IT",4)

# --------------------------------------------------------------------------------------
# class cal():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
#     def mul(self):
#         return self.a*self.b
#     def div(self):
#         return self.a/self.b
#     def sub(self):
#         return self.a-self.b
# # obj=cal(2,3)
# # print(obj.add())
# n=1
# while(n!=0)
#    a=int(input("Enter first number: "))
#    b=int(input("Enter second number: "))
#    print("1 add\nsub\n",)

# ----------------------------------------------------------














# class cal():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
#     def mul(self):
#         return self.a*self.b
#     def div(self):
#         return self.a/self.b
#     def sub(self):
#         return self.a-self.b
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# obj = cal(a, b)
# choice = 1
# while choice != 0:
#     print("0. Exit")
#     print("1. Add")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     choice = int(input("Enter choice: "))
#     if choice == 1:
#         print("Result: ", obj.add())
#     elif choice == 2:
#         print("Result: ", obj.sub())
#     elif choice == 3:
#         print("Result: ", obj.mul())
#     elif choice == 4:
#         print("Result: ", round(obj.div(), 2))
#     elif choice == 0:
#         print("Exiting!")
#     else:
#         print("Invalid choice!!")
#
# print()













