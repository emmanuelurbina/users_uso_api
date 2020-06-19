#!/usr/bin/env python
import requests
import xlsxwriter


class Spreedsheet:
    """
        Genera un archivo excel
    """
    __name_book = "usuarios"
    __default_extension = "xlsx"
    __book = ''
    __sheet = ''
    row = 0
    col = 0

    @classmethod
    def create_book(cls):
        cls.__book = xlsxwriter.Workbook(
            f"{cls.__name_book}.{cls.__default_extension}")

    @classmethod
    def create_sheet(cls):
        cls.__sheet = cls.__book.add_worksheet()

    @classmethod
    def close_book(cls):
        cls.__book.close()

    @classmethod
    def create_headers_users(cls):
        cls.__sheet.write(cls.row, cls.col, "Genero")
        cls.__sheet.write(cls.row, cls.col + 1, "Nombre")
        cls.__sheet.write(cls.row, cls.col + 2, "Email")
        cls.__sheet.write(cls.row, cls.col + 3, "Edad")

    @classmethod
    def fill_spreedsheet(cls, data):
        row = 0
        for user in data:
            name = user['name']
            age = user['age']
            gender = user['gender']
            email = user['email']
            row += 1
            cls.__sheet.write(row, cls.col, gender)
            cls.__sheet.write(row, cls.col + 1, name)
            cls.__sheet.write(row, cls.col + 2, email)
            cls.__sheet.write(row, cls.col + 3, age)


class Users:
    """
        Obtiene Usuarios de la api random user
        y devuelve un diccionario ordenados por
        edad mayor a menor
    """
    url = "https://randomuser.me/api/?results={results}&inc={fields}".format(
        results=100,
        fields="name,gender,dob,email")
    results = requests.get(url).json()
    users = []

    def get_users(self):
        print("Loading...")
        # recorremos los resutados de la petición
        for user in self.results['results']:
            title = user['name']['title']
            first = user['name']['first']
            last = user['name']['last']
            full_name = "{} {} {}".format(title, first, last)
            age = user['dob']['age']
            gender = user['gender']
            email = user['email']
            # Generamos nuevo diccionario
            self.users.append({"name": full_name,
                               "age": age,
                               "gender": gender,
                               "email": email})
            # se ordena por edad descendente
            self.users.sort(key=lambda x: x['age'], reverse=True)
        return self.users

    def download_users(self):

        users = self.get_users()
        book = Spreedsheet()
        book.create_book()
        book.create_sheet()
        book.create_headers_users()
        book.fill_spreedsheet(users)
        book.close_book()
        print("Ok")


users = Users()
users.download_users()
