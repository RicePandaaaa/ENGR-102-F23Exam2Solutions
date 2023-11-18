# Open the file
with open("item_cost.dat", "r") as input_file:
    # Skip the header
    input_file.readline()

    # Read in the lines and compare
    highest_cost = ""
    highest_name = ""

    lines = input_file.readlines()
    for line in lines:
        # Split the data
        name, cost = line.strip().split(",")
        cost = float(cost)

        # Default values
        if highest_cost == "":
            highest_cost = cost
            highest_name = name

        # Compare and check
        if highest_cost < cost:
            highest_cost = cost
            highest_name = name

    print(f"The most expensive item is {highest_name} and costs ${highest_cost:.2f}")