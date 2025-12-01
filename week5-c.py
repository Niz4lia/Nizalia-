n=int(input('Enter The no. of rows: '))
for i in range(n):
    spaces=n-i-1
    star=2*i+1
    print(" "*spaces+"*"*star)
for i in range(n-2,-1,-1):
    spaces=n-i-1
    star=2*i+1
    print(" "*spaces+"*"*star)