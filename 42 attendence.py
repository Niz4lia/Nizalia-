lst = []
rang=int(input("Enter The Quantity of Students: "))
while True:
    
    name= input("Enter a name (type done to stop): ").strip()
    if name.lower() == 'done':
        break
    if name in lst:
        print(f"{name} is already in the list.")
    else:
        lst.append(name)
        
        print(f"{name} is added.")
if lst:
        ed=str(input("Do you want to edit any name (yes/no)"))
        if ed == 'no':
            print('')

        elif ed=="yes":
            ena=str(input('Which name you want to edit: '))
            position = lst.index(ena) 
            if ena:
                ask=str(input("Edit The name: "))
                lst= [ask if x == ena else x for x in lst]
            else:
                print('Name not Found')

        rem=str(input('Do you want to remove any name?(yes/no)'))
        if rem =='no':
            print("")

        elif rem =='yes':
            re=str(input("Enter The name you want to remove: "))
            if re:
                lst.remove(re) 
            else:
                print('NAME not Found')
                
        lst.sort()
        print("\nThe Attendance is:", lst)
        print('Total no. of students: ',len(lst))
else:
    print('No students are marked present')