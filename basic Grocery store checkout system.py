name=input('Enter your name: ')
pri=[]

for i in range(1, 4):
    price=float(input(f'Enter the price of item {i}: '))
    while price<0:    
        print('Invalid price, please enter a valid (positive) value.')
        price=float(input(f'Enter the price of item {i}: '))
    else:
        pri.append(price)
        

total=sum(pri)
print(f'{name}, the total amount for your groceries is: {total}R.s')
mem=input('Do you have a membership card? (yes/no): ').strip().lower()
if mem=='yes':
    discount=total*10/100
    famount=total-discount
    print(f'You have received a 10% discount of {discount}R.s. The final amount after discount is: {famount}R.s')
else:
    print(f'No discount applied.\nThe final amount to be paid is: {total}R.s')