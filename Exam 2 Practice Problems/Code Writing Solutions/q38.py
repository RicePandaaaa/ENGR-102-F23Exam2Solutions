import numpy as np

# Read the file
with open("Exam 2 Practice Problems\\Code Writing Solutions\\data.dat", "r") as f:
    # Skip the first line
    f.readline()

    # Get the headers
    header_names = f.readline().strip()[2:].split(",")
    header_units = f.readline().strip()[3:-1].split("),(")

    # Put stuff into a numpy array
    data = []

    for line in f.readlines():
        values = line.split(",")
        for i in range(len(values)):
            values[i] = float(values[i])

        data.append(values)

    np_data = np.array(data)

    # Minimum temperature
    temperatures = np_data[:, 1]
    min_temperature = np.min(temperatures)

    # Maximum windspeed
    windspeeds = np_data[:, 2]
    max_windspeed = np.max(windspeeds)

    # Output
    print(f"Minimum temperature is {min_temperature} {header_units[1]}")
    print(f"Maximum windspeed is {max_windspeed} {header_units[2]}")
        