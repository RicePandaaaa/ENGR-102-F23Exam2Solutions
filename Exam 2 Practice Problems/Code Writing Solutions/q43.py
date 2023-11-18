# Open the file
with open("grades.txt", "w") as output_file:
    # Get number of students
    num_of_students = int(input("Enter the number of students: "))

    # Store data
    total_score = 0
    names = []
    scores = []

    # Get the name and scores
    for _ in range(num_of_students):
        next_line = input("Enter the next name and score: ")
        name, score = next_line.split()
        score = float(score)

        # Add to sum
        total_score += score

        # Add to lists
        names.append(name)
        scores.append(score)

    # Figure out the average
    score_average = total_score / num_of_students
    print(f"The average grade for this quiz is {score_average:.1f}")

    # Figure out column size
    column_size = len("Name") + 2  # Equal to 6
    for name in names:
        column_size = max(column_size, len(name) + 2)

    # Write the header line
    output_file.write(f"{'Name':<{column_size}}Score\n")

    # Write rest of lines
    for i in range(len(names)):
        output_file.write(f"{names[i]:<{column_size}}{scores[i]:.1f}\n")



