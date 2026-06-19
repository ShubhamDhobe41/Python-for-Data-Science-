# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end='')
#     print()


# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print('*',end='')
#     print()

# # find the length of given without the len()
# s = input('enter a String :')
# counter = 0
# for i in s:
#     counter += 1
# print("Length of String :",counter)


# # Extract username from a given email
'''E.g if the email is ritesh24Singh@gmail.com
   Then the username should be nitish24singh
'''
# s = input('enter a Email :')
# position = s.index('@')
# print(s[0:position])


# # count the frequency of a perticular character in provided string
''' e.g : 'hello how are you ' is  the string , the frequency of h in this string is 2 '''
# s = input('enter a Email :')
# term = input('what would like to search for :')
# counter = 0
# for i in s:
#     if i == term:
#         counter += 1
# print('frequency ',counter)


# # write a program which can remove a perticular character from a string
# s = input('enter a Character :')
# term = input('what would like to remove for :')
# result = ''
# for i in s:
#     if i != term:
#         result = result + i
# print(result)


# # write a program that can check number whether a given string is palindrome or not
# s = input('enter a String :')
# flag = True
# for i in range(0,len(s)//2):
#     if s[i] != s[len(s) - i - 1]:
#         flag = False
#         print("Not Palindrome")
#         break
# if flag:
#     print("Palindrome")

# # write a program to count the number of words in a string without split()
# s = input('enter a String :')
# L = []
# temp = ''
# for i in s:
#     if i != ' ':
#         temp = temp + i
#     else:
#         L.append(temp)
#         temp = ''
# L.append(temp)
# print(L)


# # write a program to convert a string to title case without using the title()
# s = input('enter a String :')
# for i in s.split():
#     print(i[0].upper() + i[1:].lower() , end=' ')


# # write a program that can convert an integer to string
number = int(input('enter a number :'))
digits = '0123456789'
result = ''
while number != 0 :
   result = digits[number % 10] + result
   number = number // 10
print(result)
print(type(result))


