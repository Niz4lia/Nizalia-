#Marksheet
def grade(score: int) ->str:
 if score >= 90 and score <= 100:
  return "A"
 elif score >= 80 and score <= 89:
  return"B"
 elif score >= 70 and score <= 79:
  return"C"
 elif score >= 60 and score <= 69:
  return"D"
 else:
  return "F"
n= int(input("Enter Students No.: "))
results =[]
for i in range(1, n + 1):
    name=input(f"Student{i} name: ")
    s=int(input(f"{name}'s score (0-100): "))
    results.append((name, s, grade(s)))

print("\nresults")
print("-" * 28)
for name, s, g in results:
    print(f"Name: {name:12} | score: {s:3d} | grade: {g}")