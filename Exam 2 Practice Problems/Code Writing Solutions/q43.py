# Open a file
with open("grades.txt", "w") as output_file:
    # Get number of students
    num_students = int(input("Enter the number of students: "))

    # Store each student and their grades
    student_names = []
    student_grades = []

    for _ in range(num_students):
        name, grade = input("Enter the next name and score: ").split(" ")
        grade = float(grade)

        student_names.append(name)
        student_grades.append(grade)

    # Calculate the average
    average_grade = sum(student_grades) / len(student_grades)
    print(f"The average grade for this quiz is {average_grade:.1f}")

    # Calculate column length
    name_col_len = 6

    for name in student_names:
        name_col_len = max(len(name) + 2, name_col_len)

    # Write to the file
    output_file.write(f"{'Name':<{name_col_len}}Score\n")
    for i in range(num_students):
        output_file.write(f"{student_names[i]:<{name_col_len}}{student_grades[i]:.1f} \n")