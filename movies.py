m= []
def add():
    add = input("Enter movie to add: ")
    m.append(add)
    print("Updated movie list:", m)
def rem():
    remove = input("Enter movie title to remove: ")
    m.remove(remove)
    print("Updated movie list:", m)

counts = {}
for m in m:
    letter = m[0].upper()
    if letter not in counts:
        counts[letter] = 1
    else:
        counts[letter] += 1
for i in counts:
    print(i, counts[i])
while True:  
    print('Add Movie: 1,\nRemove Movie: 2\nExit:3')
    c=input('Enter Your Choice: ')
    if c=='1':
        add()
    elif c=='2':
        rem()
    elif c=='3':
        break
    else:
        print('Error')
