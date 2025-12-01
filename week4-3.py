courses = {
    "Data Structures": {"Alice": 85, "Bob": 90, "Charlie": 75},
    "Algorithms": {"Alice": 95, "Dave": 88},
    "Machine Learning": {"Bob": 82, "Eve": 91, "Frank": 78}
}

courses["Data Structures"].update({"Alice": 90})
courses["Data Structures"].pop("Charlie")


courses.update({"Web Development": {"Grace": 92, "Henry": 85}})


if "Bob" not in courses["Algorithms"]:
    courses["Algorithms"]["Bob"] = 80


courses.pop("Machine Learning", None)


data = courses.get("Data Structures")
if data:
    average = sum(data.values()) / len(data)
    print(f"Average grade in Data Structures: {average}")
else:
    print("Data Structures course not found.")

print("\nFinal Courses:")
for course in courses:
    print(course, "=", courses[course])


