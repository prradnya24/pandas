import q1 as np
arr=np.array([1,2,3,4,5,9,45,32,11,23,45,32])
new_arr=arr.reshape(4,3)
new_arr1=arr.reshape(6,2)
print(new_arr)
print(new_arr1)


arr3d=np.array([[1,2,3],[4,5,6],[7,8,9]])
flat_arr=arr3d.flatten()
print(flat_arr)


arr2d=np.array([[1,2,3],[4,5,6]])
transpose=arr2d.transpose()
print(transpose)

a=np.array([10,20,30])
b=np.array([40,50,60])
result=np.add(a,b)
print(result)

a=np.array([10,20,30])
b=np.array([40,50,60])
result=np.subtract(a,b)
print(result)

a=np.array([10,20,30])
b=np.array([40,50,60])
result=np.multiply(a,b)
print(result)

a=np.array([10,20,30])
b=np.array([40,50,60])
result=np.divide(a,b)
print(result)

array=np.array([[10,20,30],[56,78,34]])
#np.median(array)
print(np.median(array))

print(np.mean(array))
print(np.std(array))
print(np.var(array))


x=np.array(['hello','good'])
y=np.array(['world','morning'])
result=np.char.add(x,y)
print(result)

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