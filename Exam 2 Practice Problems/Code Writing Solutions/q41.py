def is_perfect(number):
    """ Determines if number is perfect or not """

    divisors = []

    # Loop and find divisor
    for divisor in range(1, number):
        if number % divisor == 0:
            divisors.append(divisor)

    # Do the math
    return sum(divisors) == number


def main():
    """ main function """

    # Get the input
    num = input("Enter an integer: ")

    # Validate the number
    while True:
        try:
            num = int(num)

            # Check if is positive integer
            if num <= 0:
                num = input("Need a positive integer: ")
                continue

            break
        except:
            num = input("Bad input! Try again: ")

    # Do the output
    if is_perfect(num):
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")

if __name__ == "__main__":
    main()