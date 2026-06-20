#============================== Tuple ===================================
## create an tuple
## empty tuple
# t1 = ()
# print(t1)

## create tuple with single item
# t2 = (22,)
# print(t2)

## homogenous
# t3 = (1,2,3,4)
# print(t3)

## heterogenous
# t4 = (1,2,3,4,True,[1,2,3])
# print(t4)

## 2D
# t5 = (1,2,3,(4,5))
# print(t5)

## using type conversion
# t6 = tuple('hello')
# print(t6)


## Accessing item in the tuple
# t3 = (1,2,3,4)
# print(t3[0])
# print(t3[-1])

# print(t3[0:2])
# print(t3[-3:-1])
# print(t3[::-1])

# t5 = (1,2,3,(4,5))
# print(t5[-1][0])

## edit item in tuple
# t3 = (1,2,3,4)
# t3[1] = 23
# print(t3)

## adding item in tuple
## you can not add item in tuple . because tuple is immutable

## deleting an item
# print(t3)
# del t3
# print(t3) # error

# del t5[-1] # error
# print(t5)

## operation on tuple
# t1 = (1,2,3,4)
# t2 = (5,6,7,8)
# print(t1 + t2 )
# print(t1 * 2)


# print(1 in t1)
# print(1 not in t1)


##  loop
# for i in t1:
#     print(i)


## Tuple function
# t1 = (1,2,3,4)
# print(len(t1))
# print(sum(t1))
# print(min(t1))
# print(max(t1))
# print(sorted(t1))
# print(sorted(t1,reverse=True))
# print(t1.count(5))
# print(t1.count(2))
# print(t1.index(5)) #error
# print(t1.index(2))


## unpacking
# a,b,c = (1,2,3)
# print(a,b,c)

# a,b = (1,2,3)
# print(a,b) # error

# a,b,*others = (1,2,3,4)
# print(a,b)
# print(others)

## swapping
# a = 1
# b = 2
# a,b = b,a
# print(a,b)

## Zipping tuples
# a = (1,2,3,4)
# b = (5,6,7,8)
# print(zip(a,b))
# print(list(zip(a,b)))


#============================== Set ===================================

## create sets
##  empty
# s = set()

## 1D and 2D
# s1 = {1,2,3,4}
# print(s1)

# s2 = {1,2,3,{4,5}}
# print(s2)

## heterogenous
# s3 = {1,'hello',4.5,True}
# print(s3)

## using type conversion
s4 = set([1,2,3])
# print(s4)

## duplicate not allowed
# s5 = {1,1,3,2,4,5,2,5}
# print(s5)

## set can not have mutable items
# s6 = {1,2,3,[4,5]}
# print(s6) # error

## unordered
# s1 = {1,2,3}
# s2 = {3,2,1}
# print(s1 == s2)

## Accessing and editing item is not possible

## Adding and update items
# s = {1,2,3,4,5}
# s.add(6)
# s.update([7,8,9])
# print(s)

## deleting item
# print(s)
# del s
# print(s)

# s.discard(4)
# print(s)

# s.remove(5)
# print(s)

# s.pop()
# print(s)

# s.clear()
# print(s)

## Set operations
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

# print(s1 | s2)
# print(s1 & s2)
# print(s1 - s2)
# print(s2 - s1)
# print(s1 ^ s2)
# print(1 in s1)
# print(1  not in s1)

## Or
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))

# for i in s1 :
#     print(i)


# print(len(s1))
# print(max(s1))
# print(min(s1))
# print(sum(s1))
# print(sorted(s1))

## isdisjointset / issubset / issuperset
# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# print(s1.isdisjoint(s2))

s1 = {1,2,3,4,5}
s2 = {3,4,5}
# print(s2.issubset(s1))
# print(s1.issubset(s2))


# print(s1.issuperset(s2))

# s3 = s1.copy()
# print(s3)

## frozenset
# fs = frozenset([1,2,3])
# print(fs)


## set comprehension
# res = {i for i in range(1,11)}
# print(res)

# res = {i for i in range(1,11) if i > 5}
# print(res)

#============================== Dictionary ===================================

## empty dict
# dict = {}
# print(dict)

## 1D
# d1 = {'name':'ajay','age':23}
# print(d1)

## with mixed keys
# d2 = {(1,2,3):1,'hello':'world'}
# print(d2)

## 2D
# d3 = {'name':'ajay','age':23,'marks':{'python':90,'java':80}}
# print(d3)

## using type conversion

## mutable items as keys
# d4 = {'name':'nitish',(1,2,3):2}
# print(d4)


## Accessing items
# my_dict = {'name':'ajay','age':23}
# print(my_dict['name'])
# print(my_dict['age'])

# print(my_dict.get('name'))
# print(my_dict.get('age'))

## Adding new key value pair
# my_dict['gender'] = 'male'
# print(my_dict)

# my_dict['weight'] = 89
# print(my_dict)


##  Remove key-value pair
## pop
# d = {'name':'nitish','age':32,3:3,'gender':'male','weight':65}
# print(d)
# d.pop(3)
# print(d)

# d.popitem()
# print(d)

# del d['name']
# print(d)
# del d
# print(d)

# d.clear()
# print(d)


## 2D
d3 = {'name':'ajay','age':23,'marks':{'python':90,'java':80}}
# print(d3['marks']['java'])

## add new key-value pair in 2D
# d3['marks']['CPP'] = 76
# print(d3)

## delete perticular element in 2D
# del d3['marks']['java']
# print(d3)

## editing key-value pair
# d3['age'] = 25
# print(d3)

## Dict operations
# print(d3)
# print('nitish' in d3)
# print('ajay' in d3)
# print('name' in d3)
# print()
# for i in d3:
#     print(i)
# print()
# for i in d3:
#     print(i,":",d3[i])

## Dict function
# print(len(d3))
# print(sorted(d3)) # sorted by keys
# print(sorted(d3,reverse=True)) # sorted by keys
# print(max(d3))
# print(min(d3))


# print(d3)
# print(d3.items())
# print(d3.keys())
# print(d3.values())

# d1 = {1:2,3:4,4:5}
# d2 = {4:7,6:8}
# d1.update(d2)
# print(d1)

## dict comprehension
## print 1st 10 numbers and their sqaures
# res = {i:i**2 for i in range(1,11)}
# print(res)

## using existing dict convert km to mile
# distances = {'delhi':1000,'mumbai':2000,'banglore':3000}
# print(distances.items())
# res = {key:value * 0.62 for (key,value) in distances.items()}
# print(res)

## using zip
days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
temp_c = [30.5,32.4,31.4,33.2,23.2,35.3,31.5]
{i:j for (i,j) in zip(days,temp_c)}

## using if condition
products = {'phone':10,'laptop':0,'charger':32,'tablet':0}
res = {key:value for (key,value) in products.items() if value >0 }
print(res)







