from app.connect import connect

def create(database, nome, email, cargo, salario):
    # insert new records into the table
    # this is made specifically for the database Im using

    # nome=str, email=str, cargo=str, salario=float

    try:
        # cursor to work in the database
        db_cursor = database.cursor()

        values = (nome, email, cargo, salario)
        sql_code = "INSERT INTO funcionarios (nome, email, cargo, salario) VALUES (%s, %s, %s, %s)"
        db_cursor.execute(sql_code, values)

        database.commit()

        return "Data inserted with success."
    except Exception as e:
        return f'Error inserting new data into the database: {e}'
    
if __name__ == '__main__':
    connection = connect('example123')

    if connection:
        try:
            # insert data into the table
            new_data = create(connection, 'Gabriel Venturini', 'example@example.com', 'Backend Developer', 2500.00)
            print(new_data)
        except Exception as e:
            print(f'Error while loading your requisition: {e}')