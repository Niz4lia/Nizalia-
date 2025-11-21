lst=[]
def add_student():
    name=str(input('Enter the students Name: '))
    roll=int(input('Enter the students roll no.: '))
    mark=int(input('Enter The students marks: '))
    grade=str(input('Enter THe students grade:'))
    lst.append({"name": name,"roll": roll,"marks": mark,'grade': grade})
    print('student added successfuly ')

def view():
    if not lst:
        print('no student record found')
    else:
        for n in lst:
            print(f'Roll:{n["roll"]} | Name: {n["name"]} | Marks: {n["marks"]} | Grade: {n["grade"]}')
    print()

def search():
    roll=int(input("Enter the roll no.  of student: "))
    for r in lst:
        if r['roll'] == roll:
            print(f'Found:{r}')

def update():
    roll=input('Enter roll no. to update: ')
    for n in lst:
        if n['roll']==roll:
            n['name']=input('Enter the new name')
            n['mark']=input('Enter the new mark')
            n['grade']=input('Enter the new Grade')
            print('record updated')
            return
        else:
            print('Student not found')

def delete():
    roll=(input("Enter the roll no.  of student to delete: "))
    for n in lst:
        if n['roll']==roll:
            lst.remove(n)
            print('Record deleted\n')
            return
        else:
            print('Student not found\n')

def main():
    while True:
        print('===STUDENT MANAGEMENT SYSTEM===')
        print('1.Add student')
        print('2.View student')
        print('3.Search student')
        print('4.Update student')
        print('5.Delete student')
        print('6.Exit')
        cho =input('Enter your choice')

        if cho =='1':
            add_student()
        elif cho =='2':
            view()
        elif cho =='3':
            search()
        elif cho == '4':
            update()
        elif cho== '5':
            delete()
        elif cho=='6':
            print("Good bye")
            break
        else:
            print('Invalid choice')
main()