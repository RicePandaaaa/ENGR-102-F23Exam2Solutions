# Open the file
with open("yields.txt", "a") as output_file:
    # Ask for inputs
    ideal_mass = float(input("Please enter the ideal mass: "))
    experimental_mass = float(input("Please enter the experimental (actual) mass: "))

    # Calculate yield
    percent_yield = 100 - (100 * abs((experimental_mass - ideal_mass) / ideal_mass))

    # Output to console and file
    print(f"The percent yield is {percent_yield}%")
    output_file.write(f"{percent_yield}%\n")