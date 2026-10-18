# Grading System
student_name = input("Enter the student's name: ")          
student_grade = float(input("Enter the student's grade: "))
if student_grade >= 90:
    print("has A grade.")
elif student_grade >= 80:
    print("has B grade.")
elif student_grade >= 70:
    print("has C grade.")
elif student_grade >= 60:
    print("has D grade.")
elif student_grade >= 30:
    print("has F grade.")

# calculate the average grade of the student
average_grade = student_grade
print(f"{student_name} has an average grade of {average_grade}.")
