# number is a string
def is_armstrong(number):
    """ Checks if the number is an Armstrong number """

    # Extract digits
    digits = list(number)
    for i in range(len(digits)):
        digits[i] = int(digits[i]) ** len(digits)

    # Do the math
    return sum(digits) == int(number)


def Armstrong_number(start, end):
    """ Returns list of all Armstrong numbers """

    # Loop and check
    arm_numbers = []

    for number in range(start, end+1):
        # Input for function is a string
        if is_armstrong(str(number)):
            arm_numbers.append(number)

    return arm_numbers


def main():
    """ main function """
    # Grab first number
    a = input("Enter an integer: ")

    # Validate a
    while True:
        try:
            a = int(a)

            # Check if positive
            if a <= 0:
                a = input("Need a positive integer: ")
                continue
            break
        except:
            a = input("Bad input! Try again: ")

    # Grab second number
    b = input("Enter another integer: ")

    # Validate b
    while True:
        try:
            b = int(b)

            # Check if positive
            if b <= 0:
                b = input("Need a positive integer: ")
                continue
            break
        except:
            b = input("Bad input! Try again: ")

    # Calculate start and end
    start = min(a, b)
    end = max(a, b)
    result = Armstrong_number(start, end)

    # Output
    print("Armstrong numbers:", result)


if __name__ == "__main__":
    main()

