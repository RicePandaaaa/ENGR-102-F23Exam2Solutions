# Uses grades(1).txt instead because another problem uses grades.txt

# File open
with open("grades(1).txt", "r") as input_file:
    # Extract the grades
    grades = input_file.read().strip().split("\n")

    # Convert strings to floats
    for i in range(len(grades)):
        grades[i] = float(grades[i])

    # Calculate stats
    print(f"The average is {sum(grades)/len(grades)}")
    print(f"The highest score is {max(grades)}")
    print(f"The lowest score is {min(grades)}")
