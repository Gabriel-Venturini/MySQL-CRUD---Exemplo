from app.connect import connect
import pandas as pd

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


def read(database, table:str):
    # shows the entire table
    try:
        db_cursor = database.cursor()
        
        # Creates a pandas dataframe for better visualization
        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query, con=database)
        
        # Exibe o DataFrame
        print(df)
        
        return df  # Returns dataframe to use if necessary
    
    except Exception as e:
        return f"Error viewing table data: {e}"
    

def update(database, table):
    # UPDATE {table}
    # SET {nome}='Paula Ribeiro', {email}='paula.ribeiro@email.com', {cargo}='Engenheira', {salario}=8000.90
    # WHERE id=63;

    # depois desenrolo
    pass

def delete(database, table: str, primary_key_name: str, pk_value: int):
    # delete records, the parameters are the table, the pk_name and the unique identifier
    # example: database, funcionarios, id, 3
    try:
        db_cursor = database.cursor()
        
        # Case for deleting all records when pk value is equal to 0
        if pk_value == 0:
            sql_code = f"DELETE FROM {table}"
            db_cursor.execute(sql_code)
            database.commit()
            return 'Successfully deleted all data from the table.'
        
        # Case for deleting a specific record
        elif primary_key_name != '' and pk_value != '':
            # Check if pk_value is a string, and add quotes around it if necessary
            if isinstance(pk_value, str):
                pk_value = f"'{pk_value}'"
            
            sql_code = f"DELETE FROM {table} WHERE {primary_key_name} = {pk_value}"
            db_cursor.execute(sql_code)
            database.commit()
            return 'Successfully deleted 1 data.'
        else:
            return 'Primary key name or value is empty.'
    except Exception as e:
        return f'Error deleting data: {e}'


if __name__ == '__main__':
    connection = connect('example123')

    if connection:
        try:
            # insert data into the table
            # new_data = create(connection, 'Gabriel Venturini', 'example@example.com', 'Backend Developer', 2500.00)
            # deletes everything
            # delete_data = delete(connection, 'funcionarios', '', 0)
            # deletes just one value
            # delete_single_data = delete(connection, 'funcionarios', 'id', 2)
            # views and read all data in a table
            read_data = read(connection, 'funcionarios')
            print(type(read_data))
        except Exception as e:
            print(f'Error while loading your requisition: {e}')