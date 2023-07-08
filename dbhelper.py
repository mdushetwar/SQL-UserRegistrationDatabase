import mysql.connector
import sys

class DBhelper:

    def __init__(self):

        try:
            self.connect = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='hit-db-demo'
            )

            self.mycursor = self.connect.cursor()

        except:
            print('Connection Failed! Try again!')
            sys.exit(0)

        else:
            print('Connected to Database!')

    def register(self, name, email, password):

        try:
            self.mycursor.execute(
                '''
                INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');
                '''.format(name, email, password)
            )

            self.connect.commit()

        except:
            return -1

        else:
            return 1


    def search(self, email, passowrd):

        self.mycursor.execute('''
        SELECT * 
        FROM users 
        WHERE email LIKE '{}' AND password LIKE '{}'
        '''.format(email, passowrd))

        data=self.mycursor.fetchall()

        return data





