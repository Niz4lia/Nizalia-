n=4
for i in range(n):
    space=n-i-1
    stars=2*i+1
    print (" "* space + "*" * stars)
 
for i in range(n-2,-1,-1):
    space=n-i-1
    stars=2*i+1
    print (" "* space + "*" * stars)
