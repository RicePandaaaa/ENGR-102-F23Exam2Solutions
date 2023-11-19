# Stats
total_age = 0
count = 0

max_age, max_name = "N/A", "N/A"
min_age, min_name = "N/A", "N/A"

# Get inputs
name = input("Enter a name: ")
age = int(input("Enter an age: "))

# Main loop
while age != 0:
    # Update average
    total_age += age
    count += 1

    # Update max
    if max_age == "N/A" or max_age < age:
        max_age = age
        max_name = name

    # Update min
    if min_age == "N/A" or min_age > age:
        min_age = age
        min_name = name

    # Get inputs again
    name = input("Enter a name: ")
    age = int(input("Enter an age: "))


# Outputs
average = "N/A"
if count > 0:
    average = total_age / count

print(f"The average age is {average}.")
print(f"The older person is {max_name} at age {max_age}")
print(f"The youngest perosn is {min_name} at age {min_age}")