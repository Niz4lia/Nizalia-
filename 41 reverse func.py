l=['1', '2', '3', '4', '5', '7']
l.reverse()
print(l)
l.remove('4')
for i in range(7, 4, -1):  
    ist = str(i)
    if ist in l:
        l.remove(ist)
        print(ist)

tup=('hi', 'hello', 'good morning', 'bonjour', 'bye', )
print(tup)
x,y,z,a,b=tup
tup2=('good bye','good very bye')
add=tup+tup2
print(add)

