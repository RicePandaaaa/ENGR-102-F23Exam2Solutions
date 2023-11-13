"""
You need the commented line but for the sake of example and testing,
I will make the function isprime myself in this file. Essentially,
my solution will uncomment line 8 and will not contain my implementation
of isprime
"""

# from ENGR102 import isprime 
import math 

def isprime(a):
    if a == 2:
        return True
    
    if a < 2:
        return False

    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
        
    return True

# Input validation for first number
number1 = input("Enter an integer: ")

while True:
    try:
        number1 = int(number1)
        break
    except:
        number1 = input("Bad input! Try again: ")

# Input validation for first number
number2 = input("Enter another integer: ")

while True:
    try:
        number2 = int(number2)
        break
    except:
        number2 = input("Bad input! Try again: ")

# Loop and check for primes
primes = []

for number in range(min(number1, number2), max(number1, number2)+1):
    if number % 2 == 0:
        continue
    else:
        if isprime(number):
            primes.append(number)

# Output
if len(primes) == 0:
    print("No primes found!")
else:
    print(f"Primes: {primes}")
