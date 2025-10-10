#Grade 
total=int(input("Enter total Number of Students: "))

for i in range(total):
 name=str(input("Enter the Student's Name: "))
 perc=int(input("Enter the Student's Percentage: "))

 if perc >= 90 and perc <= 100:
  print("A")
 elif perc >= 80 and perc <= 89:
  print("B")
 elif perc >= 70 and perc <= 79:
  print("C")
 elif perc >= 60 and perc <= 69:
  print("D")
 elif perc >100:
  print("Invalid")
 else:
  print("F")

 
  