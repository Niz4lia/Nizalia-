lst = []
while True:
  
   name= input("Enter a name (type done to stop): ").strip()
   if name.lower() == 'done':
        print(f'Attendance List={lst}')
        break
   if name in lst:
       print(f"{name} is already in the list.")
   else:
       lst.append(name)
       print(f"{name} is added.")
       
       
