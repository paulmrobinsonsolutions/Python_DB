
# Set the below to your desired server and database
def getConnection(server="localhost", database="Characters"):
    '''
    base: Database connection string for pyodbc sampler to connect to SQL Server
          with a local database named "Characters"
 
    returns: connection string
    '''
    
    #ODBC Driver 18 for SQL Server --> Error 'not trusted'
    connStr = f"""
  DRIVER={{SQL Server Native Client 11.0}};
  SERVER={server};
  DATABASE={database};
  Trusted_Connection=yes;
"""
    return connStr

def getSysTablesQuery():
    '''
    base: Generic query to get all system tables in the specified database
 
    returns: string
    '''
    return "SELECT [Name], object_id, type_desc, create_date, modify_date FROM sys.tables WITH (NOLOCK)"

def addNumbers(a, b):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if a is None or b is None:
        return 0
    
    result = a ** b
    return result

def getEvenNumbers(numbers):
    '''
    base: list of int.
    
    returns: list of int, even numbers from input list
    '''
    even_nums = [num for num in numbers if not num % 2]
    return even_nums
