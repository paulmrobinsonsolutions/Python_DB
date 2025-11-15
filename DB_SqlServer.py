# python -m pip install pyodbc
# python -m pip install --upgrade pip
import pyodbc
from DB_Constants import *

#from ast import Try
#https://docs.microsoft.com/sql/connect/python/python-driver-for-sql-server
#https://pypi.org/project/pyodbc

class DbClass(object):
    pass

def main():
    '''
    base: Simple database connection and query example
 
    returns: Name of all system tables in the specified database
    '''

    print()
    print("Let's get it started in here!")
    cursor = None

    # Get conn string from DB_Constants.getConnection()
    connStr = getConnection()
    
    try:
        print('Setting DB connection...')
        conn = pyodbc.connect(connStr)
        print('   Connected...')
        cursor = conn.cursor()

    except pyodbc.DatabaseError as e:
        print(f'ERROR: Could not open database: {e}')
        exit(1)
    except pyodbc.Error as e:
        print(f'ERROR: Some generic error occurred: {e}')
        exit(1)

    try:
        cursor.execute(getSysTablesQuery())

        # Get all tables in specified database
        for row in cursor.fetchall():
        # Get all columns in specified table
        #for row in cursor.columns(table='Director'):
            print(f'The row is: {row}')

    except pyodbc.DatabaseError as e:
        print(f'ERROR: Unexpected database error: {e}')
        exit(1)
    except pyodbc.Error as e:
        print(f'ERROR: Some generic error occurred: {e}')
        exit(1)

    cursor = None

    print()
    print("Alright! Looks like our work is done here ;)")

    # Just some silly math testing
    result = addNumbers(3, 6)
    print("The result is: ", result)

if __name__ == "__main__":
    main()


