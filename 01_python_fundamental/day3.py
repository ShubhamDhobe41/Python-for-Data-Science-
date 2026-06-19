# -------------String
# s = 'hello'
# s = "hello"
# s = '''hello'''
# s = """hello"""
# s = str('hello')
# print(s)
# print("it's new string")


# s = 'hello world'
# print(s[0])
# print(s[4])
# print(s[-1])


# print(s[0:5])
# print(s[0:])
# print(s[:4])
# print(s[:])


# print(s[::2])
# print(s[0:4:2])
# print(s[6:0:-1])

# print(s[::-1])

# print(s[-5:])
# print(s[-1:-6:-1])

# Python String are immutable
# s[0]='H'
# print(s)


# del s
# print(s)

# ------------ Operations On Strings
# Arithmatic operator
# print('delhi '+ ' mumbai')
# print('delhi '* 5)


# Relational operator
# print('delhi '== 'mumbai')
# print('delhi '> 'mumbai')
# print('delhi '< 'mumbai')


# logical operator
# print('hello' and 'world')
# print('hello' or 'world')

# loops
# for i in 'hello':
#     print(i)

# membership
# print('D' in 'Delhi')


# String functions
s = 'welcome to hello world'
# print(len(s))
# print(max(s))
# print(sorted(s))
# res = sorted('hello',reverse=True)
# print(res)

# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.swapcase())

# print(s.count('o'))
# print(s.find('is'))
# print(s.index('is'))
# print(s.endswith('d'))
# print(s.startswith('w'))
name = "ajay"
age = 25
# print(f'my name is {name} and my age is {age}')

# new way
# print('my name is {} and my age is {}'.format("ajay",25))
# print('my name is {1} and my age is {0}'.format(25,"ajay"))


# # alhanumeric check
# print("shubham123".isalnum())
# print("shubham123%".isalnum())

# # check its digit or not
# print("shubham".isalpha())
# print("12345".isdigit())


# # check its identifier or not
# print('first-name'.isidentifier())
# print('first_name'.isidentifier())
# print('name'.isidentifier())
# print('1name'.isidentifier())


# # split / join
# print('hi my name is shubham'.split('i'))
# print('hi my name is shubham'.split(' '))

# print("-".join('hi my name is shubham'))


# # Replace
# print('hi my name is shubham'.replace('shubham','ajay'))
# print('hi my name is shubham'.replace('shubham123','ajay'))

# # Strip
# print('       hi my name is shubham             '.strip())
# print('hi my name is shubham             '.rstrip())
# print('           hi my name is shubham'.lstrip())