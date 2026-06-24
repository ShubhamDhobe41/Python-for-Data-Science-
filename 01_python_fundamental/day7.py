
# map
numbers = [1, 2, 3, 4, 5]
# without map
result = []
for i in numbers:
    result.append(i * i)
# print(result) #[1, 4, 9, 16, 25]

# with map and lambda :
res = map(lambda x :x*x,numbers)
# print(list(res))

# with map and normal function :
def square(x):
    return x*x
res = map(square,numbers)
# print(list(res))

# map with multiple itrable :
num1 = [1,2,3]
num2 = [4,5,6]
res = map(lambda x,y:x+y,num1,num2)
# print(list(res))

# converting String into int
numbers = ['1','2','3','4','5']
res = map(int,numbers)
print(list(res))
print(type(res))
