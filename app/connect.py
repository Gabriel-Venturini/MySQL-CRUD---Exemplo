import mysql.connector

def connect(pwd=str):
    # connects to the database
    # the param is to make transactions safer asking for the pwd
    # every time the user tries to connect

    try:
        database = mysql.connector.connect(
            host="localhost",
            user="root",
            password=pwd
        )
        return database
    except Exception as e:
        return(e)
    

if __name__ == "__main__":
    print(connect('example123'))