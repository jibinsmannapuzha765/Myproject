class Person:
    def details(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def printdata(self):
            print(self.name)
            print(self.age)
            print(self.sex)
class Emp(Person):
    def det(self,resign,salary):
        self.resign=resgin
        self.salary=salary
    def prints(self):
        print(self.resign)
        print(self.salary)
per=Person()
per.details("anu",23,"fem")
per.printdata()
st=emp()
st.det(25,"mount")
st.prints()