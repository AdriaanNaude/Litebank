import sqlite3
# import main

connect = sqlite3.connect('client.db')

c = connect.cursor()

# c.execute('''CREATE TABLE clients (
#         first_name text,
#         last_name text,
#         age integer,
#         id integer,
#         email text
#     )''')

# c.execute("INSERT INTO clients VALUES (?,?,?,?,?)", main.register_Form())

c.execute('SELECT * FROM clients')
print(c.fetchall())


connect.commit()

connect.close()
