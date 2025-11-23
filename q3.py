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


array1=np.array([1,2,3,4,5,6])
array2=np.array([[1,2,3],[4,5,6]])
array3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(array1[3])

print('Third element in the first row',array2[0,2])
print('Third element in the second row',array2[1,1])

print('Third element in the third row',array2[1,2])

#slicing
rating=np.array([1,2,3,4,5,6])
print(rating[1:7])


books=np.array(["physics","chem","bio"])
print(books[0:2])

