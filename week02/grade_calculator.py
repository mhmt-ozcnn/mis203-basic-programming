
total_student = 0 #for counting total student.
total_score = 0 #for holding each student score total.
print("If you want to end iteration write 'q' student name part!!! ")
while True: #its infinite loop using 'TRUE' 
    student_name = input("What is your name: ") # for each student it must be in iteration

    if student_name == "q": 
        break
    student_score = int(input("What is your score: "))

    if student_score < 0 or student_score > 100:
        print("Invalid score. Please enter a number between 0 and 100. ")
        continue # this moves the iteration to the next step
    
    if student_score == 0 or student_score <= 59 :
        print(f"{student_name}: {student_score} -> F")

    elif student_score == 60 or student_score <= 69:
        print(f"{student_name}: {student_score} -> D")
    
    elif student_score == 70 or student_score <= 79:
        print(f"{student_name}: {student_score} -> C")

    elif student_score == 80  or student_score <= 89:        
        print(f"{student_name}: {student_score} -> B")

    else :        
        print(f"{student_name}: {student_score} -> A")
    
    total_student+=1 #for counting each student

    total_score += student_score #total student score.

print("Total students: ",total_student)#for show total student.
if total_student == 0:
    print("No students entered.")
print("Average Score: ",(total_score/total_student))#for show average score.

