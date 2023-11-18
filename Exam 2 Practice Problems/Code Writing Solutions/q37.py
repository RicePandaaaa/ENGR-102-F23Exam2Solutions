from ENGR102 import isprime

# Get input for a
a = input("Enter an integer: ")

# Keep re-asking until a is a valid integer
while True:
    try:
        a = int(a)
        break
    except:
        a = input("Bad input! Try again: ")

# Get input for b
b = input("Enter another integer: ")

# Keep re-asking until b is a valid integer
while True:
    try:
        b = int(b)
        break
    except:
        b = input("Bad input! Try again: ")

# Calculate start and end
primes = []
start = min(a, b)
end = max(a, b)

# Loop through start and end inclusive and check for primes
for num in range(start, end+1):
    if num % 2 == 1 and isprime(num):
        primes.append(num)

# If list exists, output it
if len(primes) > 0:
    print("Primes:", primes)

# If list is empty, let the user know
else:
    print("No primes found!")