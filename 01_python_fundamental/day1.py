# why python for DS:
''' easy to learn
  proximity with math
  community support  '''


#--------- print the data
# python is case sensitive language
# print("hello world")
# print("hello",22,3,2.3,True)
# print("hello",22,3,2.3,True , sep='/')
# print("hello",22,3,2.3,True , sep='-')


# print("hello")
# print("world")
# print("hello" ,end="-")
# print("world")


#---------- datatypes
# 1. Interger:
# print(8)
# print(1e309)

# 2. Float:
# print(2.3)

# 3. String:
# print("hello world")

# 4. Boolean:
# print(True)
# print(False)

# 5. None:
# print(None)

# 6. Complex:
# print(2+3j)

# 7. List:
# print([1,2,3,4,5])

# 8.Tuple
# print((1,2,3,4,5))

# 9.Set
# print({1,2,3,4,5})

# 10. Dict
# print({"name":"john","age":30})


# -----Type Function
# print(type(8))
# print(type(3.4))
# print(type("hello world"))
# print(type(True))


# -----Variables
name = "ajay"
a = 4
b = 4
c = 2
# print(a,b,c)
# print(a + b)
a,b,c = 4,4,2
# print(a,b,c)

a=b=c = 5
# print(a,b,c)


# static typing-c/c++/java
# int a = 23

# static binding
# int a = 5

# dynamic typing
# a = "hello"

# dynamic binding
# d = 4
# print(d)
# d = "hello"
# print(d)

#-------- keywords in python
# identifiers in python

# you can not start wit digit
name2 = "students"
# print(name2)

# you can use _ in variable name
# first-name = "ajay" # wrong
first_name = "ajay"
# print(first_name)

_ = "underscore"
# print(_)

# identifier not be keywords
# True = "ajay" # wrong
# print(True)



#---------- User Input :
# data = input("enter your input :")
# print(data)


# take input from use and store in variable , add the two variable , print the result
# num1 = int( input("Enter number 1 :"))
# num2 = int(input("Enter number 2 :"))
# print(num1 + num2)

# ----------------Type conversion
# implicit

# print(5+5.6)
# print(type(5))
# print(type(5.6))
# print(type(5+5.6)) # convert implicit

# Explicit

num = int(5.6)
# print(type(num))
# print(num)

str1 = str(5)
# print(str1)
# print(type(str1))


#---------Literals

a = 0b1010 # binary literal
# print(a)
b = 0o12 # octal literal
# print(b)
c = 100 # decimal literal
# print(c)
d = 0x1A # hexadecimal literal
# print(d)

float1 = 10.5
float2 = 1.5e2 # 1.5 * 10^
float3 = 1.5e-3

# print(float1)
# print(float2)
# print(float3)



string1 = 'this is python'
string2 = "This is python"
char = "C"
multi_str = """This is a multiline string"""
raw_str = r"This is a raw string \n with new line"
unicodes = u"This is a unicode string \u00A9 with copy right symbol"

# print(string1)
# print(string2)
# print(char)
# print(multi_str)
# print(raw_str)
# print(unicodes)


a = True + 10 # True = 1
b = False + 10 # False = 0
# print("a :",a)
# print("b :",b)

a = None
# print(a)










