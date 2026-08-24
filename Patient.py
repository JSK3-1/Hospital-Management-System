class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode):
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptoms = []

    def full_name(self):
        return f"{self.__first_name} {self.__surname}"

    def get_doctor(self):
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def add_symptom(self, symptom):
        self.__symptoms.append(symptom)

    def print_symptoms(self):
        if len(self.__symptoms) == 0:
            print("No symptoms recorded")
        else:
            for symptom in self.__symptoms:
                print(symptom)

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'