# ------------------- Operators

# Arithmetic Operators
a = 10
b = 3
# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Floor Division:", a // b) # Integer division . output will in integer
# print("Modulus:", a % b)
# print("Exponentiation:", a ** b)


# Relational Operators
x = 5
y = 10
# print("Equal to:", x == y)
# print("Not equal to:", x != y)
# print("Greater than:", x > y)
# print("Less than:", x < y)
# print("Greater than or equal to:", x >= y)
# print("Less than or equal to:", x <= y)


# Logical Operators
p = True
q = False
# print("Logical AND:", p and q)
# print("Logical OR:", p or q)
# print("Logical NOT:", not p)

# Bitwise Operators
m = 5  # In binary: 0101
n = 3  # In binary: 0011
# print("Bitwise AND:", m & n)
# print("Bitwise OR:", m | n)
# print("Bitwise XOR:", m ^ n)
# print("Bitwise NOT:", ~m)
# print("Left Shift:", m << 1)
# print("Right Shift:", m >> 1)

# Assignment Operators
c = 10
c += 5  # Equivalent to c = c + 5
# print("After += operator:", c)
c -= 3  # Equivalent to c = c - 3
# print("After -= operator:", c)
c *= 2  # Equivalent to c = c * 2
# print("After *= operator:", c)
c /= 4  # Equivalent to c = c / 4
# print("After /= operator:", c)
# c //= 2  # Equivalent to c = c // 2
# print("After //= operator:", c)

# membership operators
my_list = [1, 2, 3, 4, 5]
# print(3 in my_list)
# print(6 in my_list)
# print(3 not in my_list)


# find sum of 3 digit number entered by user
# number = int(input('Enter a three-digit number:'))
# num1 = number % 10 # get last number
# number = number // 10
# num2 = number % 10
# number = number // 10
# num3 = number % 10

# print(num1 + num2 + num3)


# ------------If - Else Operator
# email = input('enter email : ')
# password = input('enter password : ')
# if email == "example@123" and password == "12345":
#     print("Login successful!")
# elif email == "example@123" and password != "12345" :
#     print("Incorrect password. Please try again.")
#     password = input('Enter password again')
#     if password == "12345":
#         print("Login successful!")
#     else:
#         print("Incorrect password. Please try again later.")
# else:
#     print("Invalid email or password. Please try again.")


# find the min of 3 given numbers
# num1 = int(input('Enter first number : '))
# num2 = int(input('Enter second number : '))
# num3 = int(input('Enter third number : '))
# if num1 < num2 and num1 < num3:
#     print(num1, "is the smallest number.")
# elif num2 < num1 and num2 < num3:
#     print(num2, "is the smallest number.")
# else:
#     print(num3, "is the smallest number.")


# menu driven calculator
# fnum = int(input('Enter first number : '))
# snum = int(input('Enter second number : '))
# operation = input('enter the operation :')
# if operation == '+':
#     print("Result:", fnum + snum)
# elif operation == '-':
#     print("Result:", fnum - snum)
# elif operation == '*':
#     print("Result:", fnum * snum)
# else:
#     print("Result:", fnum / snum)


# menu = input("""
#
# Hi how can I help You !
# 1. Account Information
# 2. Transaction History
# 3. Transfer Funds
# 4. Exit
# Please enter the number corresponding to your choice: """)
# if menu == '1':
#     print("Account Information: Your account balance is $1000.")
# elif menu == '2':
#     print("Transaction History: You had a deposit of $500 on 01/01/2024.")
# elif menu == '3':
#     print("Transfer Funds: Please enter the amount you want to transfer."
#             "Transfer successful!")
# else:
#     print("Thank you for using our services. Goodbye!")


# ------------------ modules in python : math , keywords , datetime ,  random
# math module
# import math
# print(math.sqrt(3))
# print(math.factorial(5))
# print(math.floor(6.8))
# print(math.ceil(6.8))

# import keyword
# print(keyword.kwlist)

import random
# print(random.randint(1, 100))
# print(random.randrange(1, 100, 2))

import datetime
# print(datetime.datetime.now())

# check modules
# print(help('modules'))


# --------------- while Loops
# number = int(input('enter a number '))
# i = 1
# while i < 11:
#     print(number, 'x', i, '=', number * i)
#     i += 1
# else:
#     print('Loop completed!')


# -------------- for loop
# for i in range(1,11):
#     print(i)

# for i in range(1,11,3):
#     print(i)

# for i in range(11,0,-1):
#     print(i)

# for i in 'welcome':
#     print(i)

# for i in [1,2,3,4,5]:
#     print(i)

# for i in (1,2,3,4,5):
#     print(i)


# the current population of a town is 10000 the population of town is increesing at the rate of 10 % per year . you have to write a program to find the population at the end of each of the last 10 years
# curr_population = 10000
# for i in range(10,0,-1):
#     print(i,curr_population)
#     curr_population = curr_population - 0.1 * curr_population

#--------- Nested loops
# for i in range(1,5):
#     for j in range(1,5):
#         print(i, j)

#----------- pattern
# rows = int(input('enter number of rows '))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()


#----------- pattern
# rows = int(input('enter number of rows '))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     for k in range(i-1,0,-1):
#         print(k,end='')
#     print()

#-------- Break
# for i in range(1,11):
#     if i == 5:
#         # break
#     print(i)

# ------------check Prime number between range
# lower = int(input('Enter lower range'))
# upper = int(input('Enter Upper Range '))
# for i in range(lower,upper+1):
#     for j in range(2,i):
#         if i%j ==0:
#             break
#     else:
#         print(i)


# --------Continue
# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)


#--------Pass
# class Student:
#     pass



