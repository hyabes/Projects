import psycopg2 #to interact with postgreSQL
from db_functions import connect, get_connection, disconnect

def list_all ():
    try:
        connect()
        connection = get_connection()
        if connection is None:
            print("No active database connection. Attempting to connect...")
            connect()
            if connection is None:
                print("Failed to establish connection to database")
                return
            
        crsr = connection.cursor()

        crsr.execute("SELECT * FROM recipe_data") #TESTLINE
        rows = crsr.fetchall() #display all found

        for row in rows: #loops through rows
            print(row) #prints each row

        crsr.close()
    except Exception as error:
        print(f"Error executing query: {error}")
        disconnect()
    finally:
        if connection is not None:
            disconnect()

def list_ingredients ():
    try:
        connect()
        connection = get_connection()
        if connection is None:
            print("No active database connection. Attempting to connect...")
            connect()
            if connection is None:
                print("Failed to establish connection to database")
                return
            
        crsr = connection.cursor()

        crsr.execute("SELECT ingredients FROM recipe_data") #TESTLINE
        rows = crsr.fetchall() #display all found

        for row in rows: #loops through rows
            print(row) #prints each row

        crsr.close()
    except Exception as error:
        print(f"Error executing query: {error}")
        disconnect()
    finally:
        if connection is not None:
            disconnect()

def list_key_words ():
    try:
        connect()
        connection = get_connection()
        if connection is None:
            print("No active database connection. Attempting to connect...")
            connect()
            if connection is None:
                print("Failed to establish connection to database")
                return
            
        crsr = connection.cursor()

        crsr.execute("SELECT keywords FROM recipe_data") #TESTLINE
        rows = crsr.fetchall() #display all found

        for row in rows: #loops through rows
            print(row) #prints each row

        crsr.close()
    except Exception as error:
        print(f"Error executing query: {error}")
        disconnect()
    finally:
        if connection is not None:
            disconnect()

if __name__ == "__main__": #WHATS BEING EXECUTED
    list_all()