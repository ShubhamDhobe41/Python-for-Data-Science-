# ----------------Lists in python

a = 10
b = 20

numbers = [a, b]

# print(id(a))
# print(id(b))


list1 = [1, 2, 4, 5]
# print(id(list1))
# print(id (list1[0]))
# print(id(list1[1]))
# print(id(1))
# print(id(2))


l1 = [1, 2, 3]
l2 = [3, 2, 1]

# print(l1 == l2)# ordered

# heterogenous , duplicate
l3 = [1, 2, 3, 'a', 3]
# print(l3)
# print(l3[0]) # acessing


# ----------------------create an list
# print([])
# print([1,2,3,4,5,6])
# print([1,2,3,4,5,6,[7,8]])
# print([[[1,2],[3,4]],[[5,6],[7,8]]])
# print([1,True,4.6,'hello'])
# print(list('hello'))


# -------------------Accessing item from list
l = [1, 2, 3, 4, 5]
# print(l[0])
# print(l[-1])

l1 = [1, 2, 3, [4, 5]]
# print(l1[-1][-2])
# print(l1[3][0])

l2 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# print(l2[0][1][1])
# print(l2[0][0][1])


# -----------------Slicing
L = [1, 2, 3, 4, 5]
# print(L[0:3])
# print(L[0:])
# print(L[-3:-1])
# print(L[::2])
# print(L[-5:-2:2])
# print(L[::-1])


# ---------------- Adding item in the list
L = [1, 2, 3, 4, 5]
# L.append(6)
# print(L)

# L.append([6,7,8])
# print(L)

# L.extend([7,8])
# print(L)

# L.extend(6)
# print(L) # error

# L.extend('delhi')
# print(L)

# L.insert(2,9)
# print(L)

# L.insert(2,[3,4])
# print(L)

# editing item in the list
# L[0] = 54
# print(L)

# L[-1] = 62
# print(L)

# L[1:4] = [200,300,400]
# print(L)

# ------------------ deleting items form list
L = [2, 3, 4, 5, 6, 7, 8]
# print(L)
# del L
# print(L)

# indexing
# del L[-1]
# print(L)

# slicing
# del L[1:4]
# print(L)


# L.remove(5)
# print(L)

# L.pop(2)
# L.pop()
# print(L)

# L.clear()
# print(L)

# Operations
# arithmatic
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
# print(l1 + l2 )
# print(l1 * 3 )

l3 = [1, 2, 3, 4, 5]
l4 = [1, 2, 3, 4, [5, 6]]

# print(5 not in l3)
# print(5 in l3)
# print(5 in l4)
# print([5,6] in l4)

# list functions
l3 = [1, 2, 3, 4, 5]
# print(len(l3))
# print(min(l3))
# print(max(l3))
# print(sorted(l3))
# print(sorted(l3,reverse=True))

l5 = [1, 2, 1, 3, 4, 1, 5]
# print(l5.count(1))
# print(l5.count(2))

# print(l5.index(2))
# print(l5.index(5))

# l5.reverse()
# print(l5)

# l5.sort()
# print(l5)

l6 = [2, 1, 4, 5, 2, 6]
# print(l6)
# print(sorted(l6))
# print(l6)
# l6.sort()
# print(l6)

# print(id(l6))
# l7 = l6.copy()
# print(l7)
# print(id(l7))


# List comprehension

# l = []
# for i in range(1,11):
#     l.append(i)
# print(l)

# l = [i for i in range(1,11)]
# print(l)

## using for loop
v = [2, 3, 4]
s = 3
# x = []
# for i in v:
#     x.append(i * s )
# print(x)

## using list comprehension
# n = [s*i for i in v]
# print(n)

## add sqaure
# l = [1,2,4,5,6]
# print([i ** 2 for i in l])

# # print all number divisible by 5 in range of 1 to 50
s = [i for i in range(1, 51) if i % 5 == 0]
# print(s)

# # find language which start with letter p
# languages = ['java','python','php','c','javascript']
# res = [language for language in languages if language.startswith('p')]
# print(res)

## nested if with list comprehnsion: add new list from my_fruits and items if the fruit exists and also starts with 'a'

basket = ['apple', 'guava', 'cherry', 'banana']
my_fruits = ['apple', 'kiwi', 'grapes', 'banana']
# res = [i for i in my_fruits if i in basket if i.startswith('a')]
# print(res)

# res = [i for i in my_fruits if i in basket and  i.startswith('a')]
# print(res)

# # traverse a list
# itemwise
# L = [1,2,3,4]
# for i in L:
#     print(i)

# indexwise
# L = [1,2,3,4]
# for i in range(0,len(L)):
#     print(l[i])


## zip()
l1 = [1, 2, 3, 4]
l2 = [-1, -2, -3, -4]
# print(zip(l1,l2))
# print(list(zip(l1,l2)))


# list can contain any kind of object
# l = [1,2,print,type,input]
# print(l)
