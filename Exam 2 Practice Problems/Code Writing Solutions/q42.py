# Open the file

with open("E:\F23Exam2PracticeSolutions\Exam 2 Practice Problems\Code Writing Solutions\item_cost.dat", "r") as f:
    # Skip the header
    f.readline()

    # Keep track of most expensive item
    highest_name = ""
    highest_cost = ""

    for line in f.readlines():
        # Split up the line
        name, cost = line.split(",")
        cost = float(cost)

        # Set the first item to most expensive
        if highest_name == "" and highest_cost == "":
            highest_name = name
            highest_cost = cost

        # Compare
        if cost > highest_cost:
            highest_name = name
            highest_cost = cost

    # Output
    print(f"THe most expensive item is {highest_name} and costs ${highest_cost:.2f}")
