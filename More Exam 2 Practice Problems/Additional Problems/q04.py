# Inputs
a = input("Enter a number: ")
b = input("Enter a number: ")

# Input validation
try:
    a = int(a)
    b = int(b)

except:
    pass

else:
    start = min(a, b)
    end = max(a, b)

    revised_start = start + (4 - (start % 4))
    total = 0

    for num in range(revised_start, end+1, 4):
        total += num

    print(f"The sum of the multiples of 4 between {start} and {end} is", total)