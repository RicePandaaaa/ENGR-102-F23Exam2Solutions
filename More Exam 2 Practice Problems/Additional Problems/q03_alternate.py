# Information
people = {}

# Get the inputs
name = input("Enter a name: ")
age = int(input("Enter an age: "))

# Validate the age
while age != 0:
    # Only possible because ages are unique
    people[age] = name

    # Get input again
    name = input("Enter a name: ")
    age = int(input("Enter an age: "))

# Do the stats
ages = list(people.keys())

if len(ages) == 0:
    print("No information.")

else:
    max_age = max(ages)
    min_age = min(ages)
    avg_age = sum(ages)/len(ages)

    print(f"The average age is {avg_age}")
    print(f"The oldest person is {people[max_age]} at age {max_age}")
    print(f"The youngest person is {people[min_age]} at age {min_age}")