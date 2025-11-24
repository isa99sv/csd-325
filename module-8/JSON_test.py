# Colton Stone, November 23, 2025, Module 8.2 Assignment

import json

with open('student.json') as j:
    students = json.load(j)


print(type(students))
print()




def studentlist(students):
    print("This is the original list of students: ")
    print()
    for values in students:
        print(values)


studentlist(students)

students.append({
    "F_Name": "Colton",
    "L_Name": "Stone",
    "Student_ID": 45564,
    "Email": "cstone.email"}, )


def updatedstudentlist(students):
    print()
    print("This is the updated list of students: ")
    print()
    for values in students:
        print(values)

updatedstudentlist(students)

with open('student.json', 'w') as update_json_file:
    json.dump(students, update_json_file,
              indent=4,
              separators=(',', ': '))

print('\nSuccessfully appended to the JSON file')




