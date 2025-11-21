ave={}
def av_sco(students_scores):
    for student, n in students_scores.items():
        ave[student] = sum(n) / len(n)
    return ave
students_scores= {
    "kamran": [85, 92, 78],
    "asif": [79, 95, 88],
    "abrar": [92, 90, 85],
    "danyial": [70, 75, 80]
}
print(av_sco(students_scores))
highest=max(ave, key=ave.get)
print("The highest average score is of:", highest, "with a score of:", ave[highest])