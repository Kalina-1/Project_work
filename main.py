class Patient:
    def __init__(self, patient_id, name, age, contact_info):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.contact_info = contact_info

# Ask user for input
patient_id = input("Enter patient ID: ")
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
contact_info = input("Enter patient contact info: ")

# Create a Patient object with user input
patient = Patient(patient_id, name, age, contact_info)

# Display patient details
print(f"\nPatient Details:")
print(f"ID: {patient.patient_id}")
print(f"Name: {patient.name}")
print(f"Age: {patient.age}")
print(f"Contact Info: {patient.contact_info}")
