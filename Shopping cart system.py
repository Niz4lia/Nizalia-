avail = {'Mango': '35$', 'Rice': '50$', 'Apples': '90$'}
cart = []

def viewpro():
    if not avail:
        print('No Items available')
    else:
        print('Available Products:')
        for item, price in avail.items():
            print(f'- {item}: {price}')

def add():
    while True:
        p = input('Enter the product you want to add to cart (type "done" to stop): ').strip()
        if p.lower() == 'done':
            break
        elif p in avail:
            cart.append(p)
            print(f'{p} added to your cart.')
        else:
            print('Product is not available.')

def remove():
    r = input('Enter the product you want to remove: ').strip()
    if r in cart:
        cart.remove(r)
        print(f'{r} removed from your cart.')
    else:
        print('Product not found in cart.')

def viewcart():
    if not cart:
        print('Your cart is empty.')
    else:
        print('Products in your cart:')
        for item in cart:
            print(f'- {item} ({avail[item]})')
            

def main():
    while True:
        print('\n=== Shopping Cart System ===')
        print('1. View Products')
        print('2. Add Products')
        print('3. Remove Products')
        print('4. View Your Cart')
        print('5. Exit')
        cho = input('Enter your choice: ').strip()

        if cho == '1':
            viewpro()
        elif cho == '2':
            add()
        elif cho == '3':
            remove()
        elif cho == '4':
            viewcart()
        elif cho == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice.')

main()