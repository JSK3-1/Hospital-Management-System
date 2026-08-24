# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient


def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin', '123', 'B1 1AB')  # username is 'admin', password is '123'

    doctors = [
        Doctor('John', 'Smith', 'Internal Med.'),
        Doctor('Jone', 'Smith', 'Pediatrics'),
        Doctor('Jone', 'Carlos', 'Cardiology')
    ]

    patients = [
        Patient('Sara', 'Smith', 20, '07012345678', 'B1 234'),
        Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB'),
        Patient('Daivd', 'Smith', 15, '07123456789', 'C1 ABC')
    ]

    discharged_patients = []

    # keep trying to login until the login details are correct
    running = False
    while True:
        if admin.login():
            running = True
            break
        else:
            print('Incorrect username or password.')

    while running:
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- View patients and discharge')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin details')
        print(' 6- Quit')

        op = input('Option: ')

        if op == '1':
            admin.doctor_management(doctors)

        elif op == '2':
            admin.view_patient(patients)

            while True:
                op2 = input('Do you want to discharge a patient(Y/N): ').lower()

                if op2 == 'yes' or op2 == 'y':
                    admin.discharge(patients, discharged_patients)

                elif op2 == 'no' or op2 == 'n':
                    break

                else:
                    print('Please answer by yes or no.')

        elif op == '3':
            admin.view_discharge(discharged_patients)

        elif op == '4':
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            admin.update_details()

        elif op == '6':
            print('Goodbye!')
            running = False

        else:
            print('Invalid option. Try again')


if __name__ == '__main__':
    main()