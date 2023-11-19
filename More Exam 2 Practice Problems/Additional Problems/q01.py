# Get input
x = float(input("Enter x: "))

# Validate x
while not (-1 < x < 1):
    x = float(input("Enter x: "))

# Summation variables
total = 0
n = 0
term = x ** n
tol = 1e-6

# Main loop
while abs(term) >= tol:
    total += term
    n += 1
    term = x ** n

print(f"With x={x}, the approximate value of 1/(1-x) is {total}")