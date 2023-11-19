# Read the file
with open("peanut.dat", "r") as input_file:
    # Extract the headers
    headers = input_file.readline().strip()

    # Clean the headers and add the ratio
    headers = headers.split()
    headers[0] = headers[0].lower()
    headers.append("Ratio")

    # Print the headers
    print(" ".join(headers))

    # Calculate the ratios
    for line in input_file.readlines():
        number, majorDia, minorDia = line.strip().split()

        ratio = float(majorDia) / float(minorDia)
        ratio = f"{ratio:.2f}"
       
        # Print the line output
        print(f"{number:^6} {majorDia:^8} {minorDia:^8} {ratio:^5}")
        
    