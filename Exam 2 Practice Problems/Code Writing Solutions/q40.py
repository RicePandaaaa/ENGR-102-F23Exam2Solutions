def is_armstrong(number):
    """ Helper function to determine if a number is an Armstrong number """

    # Break up the digits
    digits = list(str(number))

    # Check for Armstrong
    total = 0
    for digit in digits:
        total += int(digit) ** len(digits)

    return total == number


def Armstrong_number(a, b):
    """ Returns a list of Armstrong numbers between, and including, a and b"""

    armstrong_numbers = []

    # Check each number
    for num in range(min(a, b), max(a, b)+1):
        if is_armstrong(num):
            armstrong_numbers.append(num)

    return armstrong_numbers


# Input validation for first number
first_number = input("Enter an integer: ")
while True:
    try:
        first_number = int(first_number)

        # Edge case: non postiive number
        if first_number <= 0:
            first_number = input("Need a positive integer: ")
            continue

        break
    except:
        first_number = input("Bad input! Try again: ")

# Input validation for second number
second_number = input("Enter another integer: ")
while True:
    try:
        second_number = int(second_number)

        # Edge case: non postiive number
        if second_number <= 0:
            second_number = input("Need a positive integer: ")
            continue

        break
    except:
        second_number = input("Bad input! Try again: ")

# Output
print("Armstrong numbers:", Armstrong_number(first_number, second_number))