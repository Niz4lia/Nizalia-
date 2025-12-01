books = {
    'The Great Gats': 15.99,
    'To Kill a Mockingbird': 12.49,
    '1984': 10.99,
    'Pride and Prejudice': 9.99,
    'Moby Dick': 8.99
}

def backup():
    return books.copy()

def view():
    return books

def total():
    return sum(books.values())

def remove():
    re = input('Enter a book to remove: ')
    if re in books:
        price = books[re]    
        del books[re]
        print(f"The book '{re}' with price {price} has been removed.")
    else:
        print('Book not found.')

while True:
    c = int(input('1= view\n2= backup\n3= sum\n4= remove a book\n5= Exit\nEnter your choice: '))
    if c == 1:
        print("Books:", view())
    elif c == 2:
        print("Backup created:", backup())
    elif c == 3:
        print("Total Cost:", total())
    elif c == 4:
        remove()
    elif c == 5:
        print("Bye")
        break
    else:
        print("Invalid choice, try again")
