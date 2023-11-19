from math import factorial
    
# Tay_term function
def Tay_term(x, n):
    return ((-1) ** n) * (x ** (2*n)) / factorial(2 * n)

# Get x
x = float(input("Enter a x value: "))

# Main loop
n = 0
term = Tay_term(x, n)
total = 0

while abs(term) >= 0.00001:
    total += term
    n += 1
    term = Tay_term(x, n)

# Output
print(f"The cosine of {x:.2f} is {total:.4f}")