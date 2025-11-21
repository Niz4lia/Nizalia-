lst = []

while True:
  
   name= input("Enter a name (type done to stop): ").strip()
   if name.lower() == 'done':
       break
   if name in lst:
       print(f"{name} is already in the list.")
   else:
       lst.append(name)
      
       print(f"{name} is added.")


              
       lst.sort()
       print("\nThe Attendance is:", lst)
       print('Total no. of students: ',len(lst))
else:
   print('No students are marked present')      