import numpy as np

arr1 = np.array([[1,2,3],[3,4,5]])
np.save('file1', arr1) 

arr2 = np.array([[3,6,9],[7,8,9]])
# save two arrays at once
np.savez('file2', file1=arr1, file2=arr2) 

larr = np.load('file1.npy')
zmeth = np.load('file2.npz')

print(larr)
print(zmeth) 

#checcking erroe
np.seterr(divide='raise')
arra1 = np.array([[1,2,3]])
arra2 = np.array([[0,6,0]])
result=np.divide(arra1,arra2)
print(result)