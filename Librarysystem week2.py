lst = ['The Nations Voice', 'Harry Potter and the Goblet of Fire', 'The 7 Habits of Highly Effective People']

while True:
    opt = int(input('\nWhat do you want to do?\n1. Add a book\n2. Check available books\n3. Check specific book\n4. Remove a book\n(Enter 0 to exit)\n'))

    if opt == 1:
        name = input("Enter the book's name: ")
        if name in lst:
            print("The book is already in the library.")
        else:
            lst.append(name)
            print("The book has been added to the library.")

    elif opt == 2:
        print("\nFOLLOWING BOOKS ARE PRESENT IN THE LIBRARY:")
        for book in lst:
            print(  book)

    elif opt == 3:
        name = input("Enter the book's name: ")
        if name in lst:
            print("The book is available in the library.")
        else:
            print("The book is not available in the library.")

    elif opt == 4:
        name = input("Enter the book's name: ")
        if name in lst:
            lst.remove(name)
            print("The book has been removed from the library.")
        else:
            print("The book is not available in the library.")

    elif opt == 0:
        print("Exiting the program")
        break

    else:
        print("Invalid option. Please choose a number between 0 and 4.")

     