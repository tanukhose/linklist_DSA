# 1 : Write a  program to create a person class. Include attributes  like name,
# country and date of birth. Implement a method to  determine the person’s age.
# class Person:
#     def __init__(self,name,country,DOB,higth,weight,age):
#         self.name = name
#         self.country = country
#         self.DOB = DOB
#         self.higth = higth
#         self.weight = weight
#         self.age = age
#     def agep(self):
#         return "Hi my name is"+self.name+". and my age is ",self.age
# person1=Person("Tanuja","India",26,5.3,45,18)
# person2=Person("Anuja","America",20,5.2,40,20)
# print(person1.agep())
#type 2
from datetime import datetime
class Person:
    def __init__(self,name,country,DOB,higth,weight,BY):
        self.name = name
        self.country = country
        self.DOB = DOB
        self.higth = higth
        self.weight = weight
        self.BY=BY
    def agep(self):
        current_year = datetime.now().year
        return "Hi my name is"+self.name+". and my age is ",current_year-self.BY
person1=Person("Tanuja","India",26,5.3,45,2005)
person2=Person("Anuja","America",20,5.2,40,2006)
print(person1.agep())