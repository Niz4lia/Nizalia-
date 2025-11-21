import numpy as np
#rank 1 single dimentional arry
ar=np.array([1,2,3])
print(ar)

#rank 2
arr=np.array([[4,5,6],[7,8,9]])
print(arr)

tu=np.array(((4,5,6),(7,8,9)))
print(tu)

#sliced

arra = np.array([
    [-1, 2, 0, 4],
    [4, -0.5, 6, 1],
    [2.6, 0, 7, 8],
    [3, -7, 4, 2]
])

print("Initial array:\n", arra)

slia = arra[:2, ::2]
print("Array with first two rows and alternate columns (0 and 2):\n", slia)

a=np.array([[1,2],[3,4]])
b=np.array([[4,3],[2,1]])
print(a)
print(b)
print(a+b)
print(a+1)

array1=np.zeros(4)
print(array1)

array2=np.random.rand(5)
print(array2)

print(array2.dtype)

ary=np.array([1,2,3,4], dtype='int32')
print(ary,ary.dtype)

floata=ary.astype('float')
print(floata,floata.dtype)

r=np.array([[1,2],[4,3]])
rr=np.array([[3,4],[5,6]])

sum=np.add(r,rr)
print("addition: ",sum)

sq=np.sqrt(r)
print(f'Square root:{sq}')
trans=r.T
print(f'Transpose:{trans}')