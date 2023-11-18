import numpy as np

# Read the file
with open("data.dat", "r") as input_file:
    # Read the headers
    headers = []

    for i in range(3):
        headers.append(input_file.readline().strip())

    # Extract units
    units = headers[2].strip()[3:-1].split("),(")
    temp_unit = units[1].split(" ")[1]
    wind_unit = units[2]

    # Read the data
    data = input_file.readlines()

    # Clean the data
    for i in range(len(data)):
        new_line = data[i].strip()
        line_data = new_line.split(",")
        
        # Convert strings to floats
        for j in range(3):
            line_data[j] = float(line_data[j])

        data[i] = line_data

    # Make numpy array
    npData = np.array(data)

    # Get stats
    min_temp = np.min(npData[:, 1])
    max_wind = np.max(npData[:, 2])

    # Output
    print(f"Minimum temperature is {min_temp:.2f} {temp_unit}")
    print(f"Maximum windspeed is {max_wind:.2f} {wind_unit}")