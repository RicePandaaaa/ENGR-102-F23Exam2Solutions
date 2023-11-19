# Patient dictionary
patients = {}

# Get number of patients
num_of_patients = int(input("Enter the number of patients: "))

# Get input and add to dict
for _ in range(num_of_patients):
    name = input("Enter the name: ")
    symptoms = input("Enter the signs and symptoms: ")
    patients[name] = symptoms

# Get user data
patient_name = input("Enter name of patient: ")
print(f"The data for \"{patient_name}\" is: \"{patients[patient_name]}\"")