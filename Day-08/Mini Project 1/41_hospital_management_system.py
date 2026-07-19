class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Patient(Person):
    def __init__(self, name, age, illness):
        super().__init__(name, age)
        self.__illness = illness   # private variable
        self.assigned_doctor = None

    def assign_doctor(self, doctor):
        self.assigned_doctor = doctor

    def display_info(self):
        print(f"Patient Name : {self.name}, Age : {self.age}, Illness : {self.__illness}")
        if self.assigned_doctor:
            print(f"Assigned Doctor : {self.assigned_doctor.name} ({self.assigned_doctor.specialization})")
        else:
            print("No doctor assigned yet.")


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def display_info(self):
        print(f"Doctor Name : {self.name}, Age : {self.age}, Specialization : {self.specialization}")


class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.hospital_name}.")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor '{doctor.name}' added to {self.hospital_name}.")

    def display_patients(self):
        print(f"\n--- Patients in {self.hospital_name} ---")
        if not self.patients:
            print("No patients registered.")
        else:
            for patient in self.patients:
                print(patient)
                patient.display_info()
        print("-" * 40)

    def display_doctors(self):
        print(f"\n--- Doctors in {self.hospital_name} ---")
        if not self.doctors:
            print("No doctors available.")
        else:
            for doctor in self.doctors:
                doctor.display_info()
        print("-" * 40)


# Example usage
hospital = Hospital("City Hospital")

# Create doctors
d1 = Doctor("Dr. Ramesh", 45, "Cardiology")
d2 = Doctor("Dr. Anita", 38, "Neurology")

# Create patients
p1 = Patient("Sai", 20, "Heart Problem")
p2 = Patient("Priya", 25, "Migraine")

# Add doctors and patients to hospital
hospital.add_doctor(d1)
hospital.add_doctor(d2)

hospital.add_patient(p1)
hospital.add_patient(p2)

# Assign doctors to patients
p1.assign_doctor(d1)
p2.assign_doctor(d2)

# Display details
hospital.display_doctors()
hospital.display_patients()