
# Set the below to your desired server and database
def getConnection(server="localhost", database="Characters"):
    
    #ODBC Driver 18 for SQL Server --> Error 'not trusted'
    connStr = f"""
  DRIVER={{SQL Server Native Client 11.0}};
  SERVER={server};
  DATABASE={database};
  Trusted_Connection=yes;
"""
    return connStr

def getSysTablesQuery():
    return "SELECT [Name], object_id, type_desc, create_date, modify_date FROM sys.tables WITH (NOLOCK)"

def addNumbers(a, b):
    result = a + b
    return result

def getEvenNumbers(numbers):
    even_nums = [num for num in numbers if not num % 2]
    return even_nums
