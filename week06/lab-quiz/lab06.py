braches = ("Software", "Design", "Marketing")
students = []
#adding 3 student
for i in range(1, 4):
    student_name = input("What is Student name: ").strip()
    student_branches = input("Which branch student choose: ").strip()
    students.append([student_name,[student_branches]])
students.insert(0, ["Minister",["Software"]])
print(f"Total registered Student Count: {len(students)}")
leaving = input("If you want to leave write your name: ").strip()
students.remove(leaving)
#Checking student who want to leave then remove this student
finded_student = False
for student in students:
    if student[0] == leaving:
        students.remove(student)
        finded_student = True
        break

deleted_pop = students.pop()
print("The last student to leave the system: ",deleted_pop)

students.append(["Burak Tan", ["Design"]])
temporary_sorted = sorted(students)
print(temporary_sorted)
students.sort()
print(students)
