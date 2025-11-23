import numpy as np
str="Hello How are you?"
print(str)
z=np.char.replace(str,"hello","hi")
print(z)


str="Hello How are you?"
print(str)
z=np.char.upper(str)
print(z)

str="Hello How are you?"
print(str)
z=np.char.lower(str)
print(z)

x=np.array([10,23,45,67,78,99,65,43])
print(x[1:6:3])

# y=np.array([[10,23,45],[67,78,99,65,43]])
# print(y[0,2:3])

array_3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(array_3d[0,1:,1:])


z=np.array([1,2,3,4,5,6,7,8,9,10])
print(z)

x=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(x)

# u=np.array([[23,45,57],[33,23,45]],[[11,22,33],[44,55,66]])
# print(u)




