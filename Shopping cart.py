cart=[]
while True:
    print('Add Item = 1\nRemove Item = 2\nView Cart = 3\nClear All=4\nExit=5')
    choice=input('Enter Your Choice: ')
    if choice=='1':
        item=input('Enter Item to add: ')
        cart.append(item)
    elif choice=='2':
        item=input('Enter Item to remove: ')
        if item in cart:
            cart.remove(item)
        else:
            print('Item not found')
    elif choice=='3':
            cart.sort()
            print(f'Your current cart is {cart}')
            print("No. of items:",len(cart))
    elif choice=='4':
        cart.clear()
    elif choice=='5':
        print("Good Bye")
        break

    else:
        print("Error")