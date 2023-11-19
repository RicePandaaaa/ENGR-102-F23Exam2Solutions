# Number pad
pad = {"ABC": 2,
       "DEF": 3,
       "GHI": 4,
       "JKL": 5,
       "MNO": 6,
       "PQRS": 7,
       "TUV": 8,
       "WXYZ": 9}

# Get input
phone_number = input("Enter a phone number: ")

# Create the translated phone number
front, back = phone_number.split("-")

new_back = ""
for letter in back:
    for key in pad.keys():
        if letter in key:
            new_back += str(pad[key])

# Assemble the new phone number
new_number = f"{front}-{new_back[:3]}-{new_back[3:]}"
print(f"{phone_number} is equivalent to {new_number}")
