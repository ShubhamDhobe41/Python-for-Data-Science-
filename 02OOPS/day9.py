# ================ OOPS ================================
'''

write oop class to handle scenario:
a user can create and view 2d cooridinates.
the user can find out distance between two coordinates.
a user can find the distance of coordinate from origin.
a user can check if a point lies on given line
a user can find the distance between a given 2d point and a given line
'''


# how to access object attributes:
class Person:
    def __init__(self,name_input,country_input):
        self.name = name_input
        self.country = country_input

    def greet(self):
        if self.country == "India":
            print(f"Namaste {self.name}")
        else:
            print(f"Hello {self.name}")


# person = Person("John", "USA")
# print(person.country)
# print(person.name)
# person.greet()
# what if i try to access non-existent attributes
# print(person.gender) # error

# create an attribute outside class
# person.gender = "male"
# print(person.gender)

"""
Reference variable : 
Reference variable hold the address of the object in memory.
we can create an object without reference variable but we cannot access it later.
an object ca have multiple reference variables 
Assigning a new reference variable to an existing object does not create a new object

"""


class Student:
    def __init__(self, name,gender):
        self.name = name
        self.gender = gender


# Student() # create object but we cannot access it later
student = Student("Ajay","male")
# print(student)

student1 = student
# print(student1) # same memory location

# print(student.name)
# print(student1.name)

# change attribute value with the help of second object
student1.name ="manish"
# print(student.name)
# print(student1.name)


# ================ pass by reference ================================
class Person1:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
# function : outside class
def greet(person):
    print(f"Hello {person.name} and my gender is {person.gender}")
    p1 = Person1("ajay","male")
    return p1

p = Person1("nitish","male")
# pass reference
# data = greet(p)
# print(data.name)
# print(data.gender)



class Person2:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
# function : outside class
def greet(person):
    print(id(person))
    person.name = "ankit"
    print(f"Hello {person.name} and my gender is {person.gender}")


# p = Person2("nitish","male")
# print(id(p))
# greet(p)
# print(p.name) # ankit



# Mutability of object:  user defined class object are mutable
class Person3:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
# function : outside class
def greet(person):
    person.name = "ankit"
    return  person


# p = Person3("nitish","male")
# print(id(p))
# p1 = greet(p)
# print(id(p1))

