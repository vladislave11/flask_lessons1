import sqlite3

try:
    sqlite_connection = sqlite3.connect("sqlite_python_oderman.db")
    cursor = sqlite_connection.cursor()
    print('DB created and connected')
    sqlite_select_query = 'SELECT sqlite_version();'
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print('SQLite versions: ', record)
    cursor.close()
except sqlite3.Error as error:
    print('Error: ',error)

finally:
    if sqlite_connection:
        sqlite_connection.commit()
        print('DB disconnected')

try:
    sqlite_connection = sqlite3.connect("sqlite_python_oderman.db")
    sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS orders2 (
                                    pizza_name TEXT,
                                    pizza_count INTEGER,
                                    address TEXT,
                                    phone_number TEXT); '''
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print('Table Created')
    cursor.close()

except sqlite3.Error as error:
    print('Error: ', error)

finally:
    if sqlite_connection:
        sqlite_connection.commit()
        print('DB disconnected')

try:
    sqlite_connection = sqlite3.connect("sqlite_python_oderman.db")
    sqlite_create_table_query = '''  CREATE TABLE IF NOT EXISTS sqlitedb_oderman (
                                    name TEXT,
                                    price INTEGER); '''
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print('Table Created')
    cursor.close()

except sqlite3.Error as error:
    print('Error: ', error)

finally:
    if sqlite_connection:
        sqlite_connection.commit()
        print('DB disconnected')

def insert_to_database(name, price):
    try:
        sqlite_connection = sqlite3.connect("sqlite_python_oderman.db")
        cursor = sqlite_connection.cursor()
        sqlite_insert_param = ''' INSERT INTO sqlitedb_oderman
                                (name,price)
                                VALUES
                                (?,?);
                                '''
        data_tuple = (name,price)

        cursor.execute(sqlite_insert_param, data_tuple)
        print('INSERTED')
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print('Error: ', error)

    finally:
        if sqlite_connection:
            sqlite_connection.commit()
            print('DB disconnected')

insert_to_database("Poultry", 46)
insert_to_database("Salami", 51)
insert_to_database("Sausage", 92)
insert_to_database("Beef", 19)
insert_to_database("Pepperoni", 7)