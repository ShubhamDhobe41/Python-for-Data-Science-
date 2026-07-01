# ================ Encapsulation ================================
# instance variable : instance variable are public by default, we can access them outside class
#                     instance variable can be made private by adding double underscore before variable name
#                     instance variable depends on object and can be accessed by object only
class Student:
    def __init__(self, name_input, country_input):
        self.name = name_input
        self.country = country_input


student1 = Student("John", "USA")
student2 = Student("Ajay", "India")
# print(student1.name)
# print(student1.country)
# print(student2.name)
# print(student2.country)

class Atm:
    # constructor : its special function
    def __init__(self):
        self.pin = ""
        self.__balance = 0
        # self.__menu()

    def __menu(self):
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
        self.__balance = user_balance
        print("Pin Created Successfully ..........")
        self.__menu()

    def change_pin(self):
        old_pin = int(input("Enter old Pin :"))
        if old_pin == self.pin:
            new_pin = int(input("Enter new pin :"))
            self.pin = new_pin
            print("Created New Pin Successfully ..........")
            self.__menu()
        else:
            print("Incorrect Pin ")
            self.__menu()

    def check_balance(self):
        user_pin = int(input("Enter your Pin :"))
        if user_pin == self.pin:
            print("Your balance is :", self.__balance)
        else:
            print("Incorrect Pin ")
        self.__menu()

    def withdraw(self):
        user_pin = int(input("Enter the Pin :"))
        if user_pin == self.pin:
            withdraw_amount = int(input("Enter a amount :"))
            if self.__balance >= withdraw_amount:
                self.__balance -= withdraw_amount
                print("Withdraw successful and balance is ", self.balance)
            else:
                print("Insufficient balance ")
            self.__menu()
        else:
            print("Incorrect PIN")

# obj = Atm()
# obj.create_pin()
# obj.__balance = "hehehe"
# obj.withdraw()


'''
 data will be private 
 private variable give access : getter and setter 
'''


class Person:
    def __init__(self):
        # save like _Person__name like this
        self.__name = "nitish"

    def get_name(self):
        return self.__name

    def __set_name__(self, new_val):
        if type(new_val) == str:
            self.__name = new_val
        else:
            print("incorrect")


# p1 = Person()
# print(p1.get_name())
# p1.__set_name__("anil")
# p1.__set_name__(10000)
# print(p1.get_name())


p1 = Person()
# this will another new variable create
p1.__name = " ankit"
p1._Person__name = " ankit"


# print(p1.__name)


# Collections of objects
class Person1:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


p1 = Person1("nitish", "male")
p2 = Person1("ajay", "male")
p3 = Person1("mina", "female")

## store object in list
# print("Using List......")
# L = [p1,p2,p3]
# print(L)
# for i in L:
#     print(i.name, ' =',i.gender)
# print()

# print("Using Set......")
# set1 = {p1,p2,p3}
# for i in set1:
#     print(i.name, ' =',i.gender)
# print()

# print("Using Dict......")
# dict1 = {'p1':p1,'p2':p2,'p3':p3}
# for i in dict1:
#     print(dict1[i].name)


## Static keywords vs instance keyword :
"""
 Instance variable value will different  for every object
 static variable value will same for every object
 
 static variable --> class (for same thing)
 Instance variable --> object (for different each)
 
"""


class Atm:
    __counter = 1

    def __init__(self):
        self.pin = ""
        self.__balance = 0
        # using instance variable you can not implement counter
        # self.cid = 0
        # self.cid += 1

        # static variable use with class name
        self.cid = Atm.__counter
        Atm.__counter = Atm.__counter + 1

        # self.__menu()

    # for static variable getter and setter
    @staticmethod # utility functions
    def get_count():
        return Atm.__counter

    def set_count(self,new_count):
        self.__counter = new_count


    def __menu(self):
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
        self.__balance = user_balance
        print("Pin Created Successfully ..........")
        self.__menu()

    def change_pin(self):
        old_pin = int(input("Enter old Pin :"))
        if old_pin == self.pin:
            new_pin = int(input("Enter new pin :"))
            self.pin = new_pin
            print("Created New Pin Successfully ..........")
            self.__menu()
        else:
            print("Incorrect Pin ")
            self.__menu()

    def check_balance(self):
        user_pin = int(input("Enter your Pin :"))
        if user_pin == self.pin:
            print("Your balance is :", self.__balance)
        else:
            print("Incorrect Pin ")
        self.__menu()

    def withdraw(self):
        user_pin = int(input("Enter the Pin :"))
        if user_pin == self.pin:
            withdraw_amount = int(input("Enter a amount :"))
            if self.__balance >= withdraw_amount:
                self.__balance -= withdraw_amount
                print("Withdraw successful and balance is ", self.__balance)
            else:
                print("Insufficient balance ")
            self.__menu()
        else:
            print("Incorrect PIN")


# every customer unique id
c1 = Atm()
c2 = Atm()
c3 = Atm()
c4 = Atm()

# print(c1.cid)
# print(c2.cid)
# print(c3.cid)
# print(c4.cid)

c5 = Atm()
Atm.counter = "hehehe"
c6 = Atm() # make private variable
print(c6.get_count())
# c6.get_count() # takes 0 positional arguments but 1 was given
Atm.get_count()
