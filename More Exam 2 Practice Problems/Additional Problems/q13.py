# Take the coefficients
coefficients = input("Enter the coefficients: ").split()

# Function to convert to equation
def make_eq(coefficients):
    terms = []

    for i in range(len(coefficients)):
        # Make a copy of the list
        coefficients = coefficients[:]

        # Edge case: coefficient is 0
        if coefficients[i] == "0":
            continue

        sign = "+"
        # Edge case: coefficient is negative
        if int(coefficients[i]) < 0:
            sign = "-"
        # Edge case: first non zero term
        if len(terms) == 0 and int(coefficients[i]) > 0:
            sign = ""
        # Edge case: abs of coefficient is 1
        if abs(int(coefficients[i])) == 1:
            coefficients[i] = ""

        power = len(coefficients) - i - 1
        symbol = f"x^{power}"

        if coefficients[i] != "":
            symbol = str(abs(int(coefficients[i]))) + symbol

        # Edge case: power is 1
        if power == 1:
            symbol = symbol.split("^")[0]
        # Edge case: power is 0
        if power == 0:
            symbol = symbol.split("x")[0]

        # Combine
        new_term = sign + " " + symbol
        terms.append(new_term)

        # Remove space if equation starts with a -
        if terms[0].startswith("-"):
            terms[0] = "".join(terms[0].split())

    return " ".join(terms).strip()


def make_derivative(coefficients):
    """ Create new coefficients for derivative """
    # Step one is to flip
    new_cos = coefficients[::-1]

    # Step two is to convert to int and multiply
    for i in range(len(new_cos)):
        new_cos[i] = int(new_cos[i]) * i

    # Step three is to flip again
    new_cos = new_cos[::-1]

    # Step four is to shift the list
    new_cos = new_cos[:-1]

    # Convert back to strings
    for i in range(len(new_cos)):
        new_cos[i] = str(new_cos[i])

    return new_cos

print(f"The equation is {make_eq(coefficients)}")
print(f"The derivative of that equation is {make_eq(make_derivative(coefficients))}")

        