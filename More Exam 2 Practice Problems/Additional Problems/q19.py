# Take input
change = float(input("Enter the change: "))
cents = int(change * 100)

# Slowly divide and conquer
dollars = cents // 100
cents %= 100

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
pennies = cents % 5

# Output
print(f"You will need {dollars} dollar coin(s), {quarters} quarter(s), {dimes} dime(s), {nickels} nickel(s), and {pennies} penn(ies)")
