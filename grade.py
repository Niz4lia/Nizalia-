total = int(input("Enter total number of students: "))
for i in range(total):
    name = input("Enter the student's name: ")
    perc = int(input("Enter the student's percentage: "))
    if 90 <= perc <= 100:
        grade = "A"
    elif 80 <= perc <= 89:
        grade = "B"
    elif 70 <= perc <= 79:
        grade = "C"
    elif 60 <= perc <= 69:
        grade = "D"
    elif perc > 100 or perc < 0:
        print("Invalid percentage entered!")
        continue
    else:
        grade = "F"
    print(f"{name} has a percentage of {perc} and has secured {grade} grade.")