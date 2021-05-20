# a=[1,2,3]
# b=int(input("enter intex"))
# try:
#    print(a[b])
# except:
#     print("intex error")
#
# finally:
#     print("inside finally")
#
#
# class: design patten
# object: real world entity
# referance: naame that refere a menory location of an object
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#
# 2 types oy variables
#
# 1 static variable  related to class, class name
# 2 instance variable  related to methods...self

# class Student:
#     college_name="mount"
#     def studentdetails(self,name,std,age):
#         self.name=name
#         self.std=std
#         self.age=age
#     def printstu(self):
#         print(self.name)
#         print(self.std)
#         print(self.age)
#         print("college",Student.college_name)
# st=Student()
# st.studentdetails("jibin","iv",25)
# st.printstu()

class Bank:
    bank_name= "state bank"
    def newacc(self,name,age,place,id):
        self.name=name
        self.age=age
        self.place=place
        self.min=5000
        self.id=id

    def deposite(self,amound):
        self.amount=amound
        print("your",self.bank_name,"credited amound",self.amount)
        print("your current balanc",self.amount+self.min)
    def withdraw(self,amound):
        self.amount=amound
        if self.amount>=self.min:
            print("low balance")
        else:
            print("debited amound of:",self.amount)
            print("current balance",self.min-self.min)
    def printnc(self):
      print("NAME",self.name)
      print("AGE",self.age)
      print("place",self.place)
      print("id",self.id)

kk=Bank()
na=input("NAME:",)
ag=input("AGE")
pl=input("PLACE")
id=input("ID")
kk.newacc(na,ag,pl,id)
kk.deposite(5000)
kk.withdraw(100)
kk.printnc()









