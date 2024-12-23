import psycopg2 #to interact with postgreSQL
from config import config #module for database config
import time

connection = None #sets to none

def test_connect():
    global connection
    try:
        if connection is None:
            params = config() #calls config function
            time.sleep(0.75)
            print()
            print('\033[32mConnection to PostgreSQL Database\033[0m \033[38;2;255;165;0m(\033[0m\033[36;3mrecipes\033[0m\033[38;2;255;165;0m)...\033[0m')
            print()
            connection = psycopg2.connect(**params) #establishs connection with database using params from earlier

            crsr = connection.cursor() #creates cursor (bridge between code)
            
            time.sleep(0.75)

            print('\033[35mPostgreSQL Database version: \033[0m')
            crsr.execute('SELECT version()') #SQL query for version
            db_version = crsr.fetchone() 
            print(f'\033[35m{db_version}\033[0m') #displays version
            print()
        
            crsr.close() #closes cursor
            
    except(Exception, psycopg2.DatabaseError) as error: #handles errors
        print(error)
    finally:
        if connection is not None: #ensures closurer of connection with database even if error
            time.sleep(0.75)
            connection.close()
            print('\033[33mDATABASE... \033[0m\033[32mREADY\033[0m')
            print()
        
def connect():
    global connection
    try:
        if connection is None:
            params = config() 
            print()
            print("\033[33mAttempting to connect...\033[0m")
            connection = psycopg2.connect(**params)
            time.sleep(0.75)
    except(Exception, psycopg2.DatabaseError) as error: #handles errors
        print(error)
    finally:
        if connection is not None:
            print()
            print("\033[32mDatabase connected\033[0m")
            print()
            time.sleep(0.75)

def disconnect():
    global connection
    try:
        if connection is not None:
            print()
            print('\033[3m\033[31mDatabase disconnected successfully\033[0m')
            print()
            connection.close()
    except(Exception, psycopg2.DatabaseError) as error: #handles errors
        print(error)
        

def get_connection(): #test connection
    global connection
    if connection is None or connection.closed !=0:
        print("No active database connection. Attempting to connect...")
        connect()
    else:
        print("\033[3m\033[32mFound\033[0m")
        print()
        time.sleep(0.75)
    return connection

if __name__ == "__main__": #WHATS BEING EXECUTED
    test_connect()

