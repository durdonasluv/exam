import json


with open("students.json") as file:
    students = json.load(file)

highest_graded_student = max(students, key=lambda x: x["grade"])
lowest_graded_student = min(students, key=lambda x: x["grade"])
average_score = sum(x["grade"] for x in students)/len(students)

print(f"The highest graded student: {highest_graded_student["name"]} - {highest_graded_student["grade"]}")
print(f"The lowest graded student: {lowest_graded_student["name"]} - {lowest_graded_student["grade"]}")
print(f"The average score: {average_score}")