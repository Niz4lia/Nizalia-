s="Hello, Python"
#Positive Indexing
s2=s[0:5]
print(s2)

s3=s[::]
print(s3)

s4=s[:]
print(s4)

s5=s[7:]
print(s5)

s6=s[:8]
print(s6)

A='abcdefghijklmnopqrstuvwxyz'
a1=A[::2]
print (a1)

a2=A[::3]
print(a2,'\n')

#Negative Indexing

a3=A[-4:]
print(a3)

a4=A[:-4]
print(a4)

print(A[-5:-2])

#Reversing the string

print(A[::-1])

N='maham'
print(N[::-1])