# OOPS - class and Object
"""
   everything in python is object
   real world application : procedure approach to object oriented approach
   Generality to specificity :
   The main power is OOPS give power to create its own datatype
   why we use : Python to organize code into objects and classes,
                making programs easier to develop, maintain, reuse, and scale
                1. Code Reusability
                2. Better Code Organization
                3. Encapsulation (Data Security)
                4. Inheritance (Code Reuse)
                5. Polymorphism (One Interface, Many Behaviors)
                6. Abstraction (Hide Complexity)

   class : Python is a blueprint or template used to create objects.create once only
           defines the data (attributes) and behavior (methods) that objects created from the class will have.
           L = [1,2,3] here [] is a class but L is a Object
           python all datatype is object
           syntax :
           class ClassName:
               # attributes and methods
           Type :
           1. Built-in
           2. User defined

   Object : Object is a instance of a class
            contain actual data
            can create many objects
            e.g :
            phone1 = Mobile("Samsung", 25000)
            phone2 = Mobile("Apple", 80000)

            inside class all things will access i.e : object



"""


# class and object
# PascalCase
class Atm:
    # constructor : its special function
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hi how can I help You 
        1. press 1 to create a pin 
        2. press 2 to change pin 
        3. press 3 to check balance 
        4. press 4 to withdraw
        5. exit \n
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = int(input('Enter your pin :'))
        self.pin = user_pin

        user_balance = int(input("enter a balance :"))
        self.balance = user_balance
        print("Pin Created Successfully ..........")
        self.menu()

    def change_pin(self):
        old_pin = int(input("Enter old Pin :"))
        if old_pin == self.pin:
            new_pin = int(input("Enter new pin :"))
            self.pin = new_pin
            print("Created New Pin Successfully ..........")
            self.menu()
        else:
            print("Incorrect Pin ")
            self.menu()

    def check_balance(self):
        user_pin = int(input("Enter your Pin :"))
        if user_pin == self.pin:
            print("Your balance is :", self.balance)
        else:
            print("Incorrect Pin ")
        self.menu()

    def withdraw(self):
        user_pin = int(input("Enter the Pin :"))
        if user_pin == self.pin:
            withdraw_amount = int(input("Enter a amount :"))
            if self.balance >= withdraw_amount:
                self.balance -= withdraw_amount
                print("Withdraw succesful and balance is ", self.balance)
            else:
                print("Insufficient balance ")
            self.menu()
        else:
            print("Incorrect PIN")


# obj = Atm()
# obj1 = Atm()
# print(type(obj)) # <class '__main__.Atm'>


""" 
 Methods vs Function :
 inside class create - method 
 independent / outside class - function 
 
"""

"""
 Magic methods / Dunder function :special methods . each method has a power 
 __init__()
 we can create own data types using methods
 constructor : its special method, automatic call 
             use : execute when object created, use to backend config , database connection
                   and initialize variables 
 self : self is current object 
      why self in class: using self one method can access another method 
      you can write with self or other name 

"""


class Temp:
    def __init__(self):
        print("Hello")
        print(id(self))  # 2425445010512

    # def display():
    #     print("display method ")


# temp = Temp()
# temp.display()
# when self not use in method then error happen and bydefault python send one argument internally thats why
# "Temp.display() takes 0 positional arguments but 1 was given" happen
# print(id(temp)) # 2425445010512


"""
 Fraction custom data type :
 Q . why we use magic method when we work with operator also :
            Python doesn't know what adding two Student objects means.
            Python how an operator should behave for your custom objects.
            Operands are the values or objects that the operators work on.
            Magic method that tells Python how to perform + on Number objects.
"""


class Fraction:
    # Parameterized constructor
    def __init__(self, x, y):
        self.num = x
        self.den = y

    # how to represent when print object
    def __str__(self):
        return '{}/{}'.format(self.num,self.den)

    # f1 - self , f2 - other
    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return '{}/{}'.format(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return '{}/{}'.format(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return '{}/{}'.format(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return '{}/{}'.format(new_num, new_den)

    # non magic method
    def convert_to_decimal(self):
        return self.num / self.den

f1 = Fraction(3, 2)
f2 = Fraction(5,2)
print(f1)
print(f2)
# print(f1 + f2) #  without __add__() -  unsupported operand type(s) for +: 'Fraction' and 'Fraction'
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
res = f1.convert_to_decimal()
print(res)
