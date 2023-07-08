import sys
from dbhelper import DBhelper

class BrainBay:

    def __init__(self):
        self.db = DBhelper()
        self.menu()

    def menu(self):

        user_input=input(
            '''
            Please select your option:
            1. Press 1 to register
            2. Press 2 to Log-in
            3. Press anything else to exit'''
        )

        if user_input == '1':
            self.register()

        elif user_input == '2':
            self.login()

        else:
            sys.exit(1000)

    def register(self):
        name = input('Enter your name')
        email = input('Enter your email')
        password = input('Enter your password')

        response = self.db.register(name, email, password)

        if response:
            print('Registration Successful!')

        else:
            print('Registration Failed!')

        self.menu()

    def login_menu(self):

        user_input = input('''How would you like to proceed?
            1. Press 1 to see profile
            2. Press 2 to edit profile
            3. Press 3 to delete profile
            4. Press 4 to logout
        ''')

    def login(self):
        email= input('Enter your email')
        password = input('Enter your password')

        data= self.db.search(email, password)

        if len(data) == 0:
            print('Incorrect email/password!')
            self.login()

        else:
            print('Hello', data[0][1])
            self.login_menu()

    def exit(self):
        print('You are successfully logged out!')


obj=BrainBay()

