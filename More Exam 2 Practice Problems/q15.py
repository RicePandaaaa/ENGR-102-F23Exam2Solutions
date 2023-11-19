# Store the data
red = []
non_red = []

# Ask for input
color = input("Is your student red-headed (Y/N): ")
age = int(input("Enter your student's age: "))

# Add to lists
if age >= 0:
    if color == "Y":
        red.append(age)
    else:
        non_red.append(age)

# Keep asking
while age >= 0:
    # Ask for input
    color = input("Is your student red-headed (Y/N): ")
    age = int(input("Enter your student's age: "))

    # Add to lists
    if age >= 0:
        if color == "Y":
            red.append(age)
        else:
            non_red.append(age)

# Calculate the stats
red_min = str(min(red))
red_max = str(max(red))
red_len = str(len(red))

non_red_min = str(min(non_red))
non_red_max = str(max(non_red))
non_red_len = str(len(non_red))

# Write to the file
with open("Student_Data_23Fa.txt", "w") as output_file:
    # Write the column names
    output_file.write("Gender     Number of Students  Minimum Age  Maximum Age\n")

    # Write the other lines
    red_line = f"Redheaded  {red_len:<{len('Number of Students  ')}}{red_min:<{len('Minimum Age  ')}}{red_max}\n"
    output_file.write(red_line)

    non_red_line = f"Not Red    {non_red_len:<{len('Number of Students  ')}}{non_red_min:<{len('Minimum Age  ')}}{non_red_max}\n"
    output_file.write(non_red_line)