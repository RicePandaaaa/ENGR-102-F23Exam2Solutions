def perfect(num):
    """ Returns True if num is a perfect number, False otherwise"""
    # 6 is smallest perfect number so False if num < 6
    if num < 6:
        return False
    
    # Loop through all possible divisors
    divisors = []

    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)

    return sum(divisors) == num


# Input validation for first number
number = input("Enter an integer: ")
while True:
    try:
        number = int(number)

        # Edge case: non postiive number
        if number <= 0:
            number = input("Need a positive integer: ")
            continue

        break
    except:
        number = input("Bad input! Try again: ")

result = ""
if not perfect(number):
    result = "not "

# Output
print(f"{number} is {result}a perfect number")



