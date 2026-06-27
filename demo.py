# name = input("Enter a name :")
# age = int(input("Enter a age :"))
# print(age)
# print(name)
# print(f"The Name is {name} and my age is {age}")
# print("a","b","c",sep="=")


"""
This is a
multi-line comment
"""

'''
This also works
for multiple lines
'''

x = 1
x = x + 1  # adds 1 to x
price = 0
total = price * 1.18


def add(a, b):
    """returns the sum of a and b
      its docstring special comment in function
      Args:
        a: num1
        b: num2
      """


# Type conversion
x = 5
y = 2.3
res = x + y
# print(res)
# print(type(res))


x = "10"
y = int(x)
# print(y)
# print(type(y))
# try:
#     x = int(input("Enter a number: "))
# except ValueError:
#     print("That's not a valid number!")

# print("Hello\nWorld")   # \n → new line
# print("Hello\tWorld")   # \t → tab
# print("She said \"hi\") # \" → double quote")
# print("C:\\Users")      # \\ → backslash


# marks = 75
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")


# age = 20
# has_id = True
# if age >= 18:
#     if has_id:
#         print("Entry allowed")
#     else:
#         print("No ID, entry denied")
# else:
#     print("Too young to enter")


age = 20
# if age >= 18 : price("adult")
# result = "Adult" if age >= 18 else "Minor"


# WITHOUT break — else RUNS
# x = 0
# while x < 5:
#     print(x)
#     x += 1
# else:
#     print("✅ else ran!")   # prints


# WITH break — else SKIPPED
# x = 0
# while x < 5:
#     if x == 3:
#         break           # exits loop immediately
#     print(x)
#     x += 1
# else:
#     print("❌ this won't print")  # skipped!


#  Searching for an item
# numbers = [1, 5, 8, 12, 20]
# target = 8
# i = 0
# while i < len(numbers):
#     if target == numbers[i]:
#         print(f"✅ Found {target} at index {i}")
#         break
#     i += 1
# else :
#     print(f"❌ {target} not found in list")


# Login system with limited attempts
# correct_password = "python123"
# attempts = 0
# max_attempts = 3
#
# while attempts <= max_attempts:
#     password = input("Enter a password :")
#     if password == correct_password:
#         print("✅ Login successful!")
#         break
#     else:
#         attempts += 1
#         print(f"❌ Wrong! {max_attempts - attempts} attempts left")
# else:
#     print("🔒 Account locked! Too many failed attempts.")

# while True:
#     age = input("Enter your age :")
#     if age.isdigit() and 1 <= int(age) <= 120:
#         print(f"Valid Age : {age}")
#         break
#     else:
#         print("Invalid input , try Again !")
# else:
#     print("This won't execute")

# Other languages use {} for blocks
# if (age > 18) {
#     console.log("Adult");   // JavaScript
# }

# Python uses indentation instead
if age > 18:
    print("Adult")          # Python