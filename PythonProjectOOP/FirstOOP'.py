# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age
# #
# # p1 = Person("John", 36)
# #
# # print(p1.name,p1.age)
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def __str__(self):
#     return f"{self.name},{self.age}"
#
# p1 = Person("John", 36)
#
# print(p1)
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# y=Person("ami","tmi")
# x.printname()



#
# class Person:
#   def __init__(self, fname, lname,age):
#     self.firstname = fname
#     self.lastname = lname
#     self.age=age
#
#   def printname(self):
#     print(self.firstname, self.lastname,self.age)
#
# class Student(Person):
#   def __init__(self, fname, lname,age):
#     Person.__init__(self, fname, lname,age)
#
# x = Student("Mike", "Olsen",9)
# x.printname()
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  # def move(self):
  #   print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  # def move(self):
  #   print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()