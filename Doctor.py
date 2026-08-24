class Doctor:
    """Represents a doctor in the hospital system"""

    def __init__(self, first_name, surname, speciality):
        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []

    def get_first_name(self):
        return self.__first_name

    def get_surname(self):
        return self.__surname

    def get_speciality(self):
        return self.__speciality

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_surname(self, surname):
        self.__surname = surname

    def set_speciality(self, speciality):
        self.__speciality = speciality

    def full_name(self):
        return f"{self.__first_name} {self.__surname}"

    def add_patient(self, patient):
        self.__patients.append(patient)

    def get_patients(self):
        return self.__patients

    def __str__(self):
        return f"{self.full_name()} ({self.__speciality})"