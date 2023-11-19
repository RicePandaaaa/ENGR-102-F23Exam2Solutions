# Get inputs (note that both solutions use the next 4 lines)
numbers = []

for _ in range(5):
    numbers.append(int(input("Enter a number: ")))

"""
Solution 1: 

# Check for duplicates
if len(set(numbers)) != 5:
    print("Duplicates")
else:
    print("All Unique")
"""

# Solution 2
for i in range(len(numbers)-1):
    if numbers[i] in numbers[i+1:]:
        print("Duplicates")
        break
else:
    print("All Unique")