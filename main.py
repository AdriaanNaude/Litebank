import sqlite3
import os


class account():
    def __init__(self, name, surname, age, id):
        self.name = name
        self.surname = surname
        self.age = age
        self.id = id


class client(account):
    def __init__(self, name, surname, age, id, email):
        super().__init__(name, surname, age, id)
        self.email = email


def register_Form():
    name = input('Name: ')
    surname = input('Surname: ')
    age = input('Age: ')
    id = input('Id number: ')
    email = input('Email: ')

    p = client(f'{name}', f'{surname}', f'{age}',
               f'{id}', f'{email}')

    data_list = [p.name, p.surname, p.age, p.id, p.email] 

    return data_list


register_Form()
