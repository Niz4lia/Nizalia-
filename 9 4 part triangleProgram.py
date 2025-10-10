n=4
for i in range(1, n + 1):
    for j in range(1, i +1):
        print("*", end="")
    print()
for i in range(2, n + 1):
    for j in range( i-1, n):
        print("*", end="")
    print()

for i in range(1,n + 1 ):
    for space in range( n-i):
        print(" ", end="")
    for j in range(1, 1+i ):
        print("*", end="")
    print()

for i in range(2,n + 1 ):
    for space in range( i-1):
        print(" ", end="")
    for j in range(i-1 , n):
        print("*", end="")
    print()
