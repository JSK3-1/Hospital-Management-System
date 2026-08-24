from Doctor import Doctor


class Admin:
    """A class that deals with the Admin operations"""

    def __init__(self, username, password, address=''):
        self.__username = username
        self.__password = password
        self.__address = address

    def view(self, a_list):
        """print a list"""
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self):
        """A method that deals with the login"""

        print("-----Login-----")

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        if username == self.__username and password == self.__password:
            print('Login successful')
            return True
        else:
            print('Incorrect username or password')
            return False

    def find_index(self, index, doctors):
        if index in range(0, len(doctors)):
            return True
        else:
            return False

    def get_doctor_details(self):
        first_name = input('Enter the first name: ')
        surname = input('Enter the surname: ')
        speciality = input('Enter the speciality: ')
        return first_name, surname, speciality

    def doctor_management(self, doctors):
        print("-----Doctor Management-----")

        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input('Input: ')

        if op == '1':
            print("-----Register-----")

            print('Enter the doctor\'s details:')
            first_name, surname, speciality = self.get_doctor_details()

            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists = True
                    break

            if name_exists:
                return

            doctors.append(Doctor(first_name, surname, speciality))
            print('Doctor registered.')

        elif op == '2':
            print("-----List of Doctors-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index = self.find_index(index, doctors)
                    if doctor_index != False:
                        break
                    else:
                        print("Doctor not found")
                except ValueError:
                    print('The ID entered is incorrect')

            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: '))

            if op == 1:
                new_first = input('Enter the new first name: ')
                doctors[index].set_first_name(new_first)

            elif op == 2:
                new_surname = input('Enter the new surname: ')
                doctors[index].set_surname(new_surname)

            elif op == 3:
                new_spec = input('Enter the new speciality: ')
                doctors[index].set_speciality(new_spec)

            else:
                print('Invalid option')

        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')

            try:
                doctor_index = int(doctor_index) - 1
                if self.find_index(doctor_index, doctors):
                    doctors.pop(doctor_index)
                    print('Doctor deleted.')
                    return
            except ValueError:
                pass

            print('The id entered is incorrect')

        else:
            print('Invalid operation choosen. Check your spelling!')

    def view_patient(self, patients):
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            patient_index = int(patient_index) - 1
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return
        except ValueError:
            print('The id entered is incorrect')
            return

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms()

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            doctor_index = int(doctor_index) - 1

            if self.find_index(doctor_index, doctors) != False:
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                print('The patient is now assign to the doctor.')
            else:
                print('The id entered was not found.')

        except ValueError:
            print('The id entered is incorrect')

    def discharge(self, patients, discharge_patients):
        print("-----Discharge Patient-----")

        patient_index = input('Please enter the patient ID: ')

        try:
            patient_index = int(patient_index) - 1
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return
        except ValueError:
            print('The id entered is incorrect')
            return

        discharge_patients.append(patients.pop(patient_index))
        print('The patient has been discharged.')

    def view_discharge(self, discharged_patients):
        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)

    def update_details(self):
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            username = input('Enter the new username: ')
            self.__username = username

        elif op == 2:
            password = input('Enter the new password: ')
            if password == input('Enter the new password again: '):
                self.__password = password

        elif op == 3:
            address = input('Enter the new address: ')
            self.__address = address

        else:
            print('Invalid option')