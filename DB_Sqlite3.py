#cmd> py -m pip install pyodbc
#import pyodbc as odbc
import sqlite3

#from ast import Try
#https://docs.microsoft.com/sql/connect/python/python-driver-for-sql-server
#https://pypi.org/project/pyodbc


class my_class(object):
    pass

def main():

    db = None
    cur = None
    try: 
        db = sqlite3.connect(":memory:")
        cur = db.cursor()
        print('Connected...')

    except sqlite3.Error as e:
        print(f'Could not open database: {e}')
        exit(1)

    qry_create_table = '''CREATE TABLE IF NOT EXISTS Actor (
       id INTEGER PRIMARY KEY,
       first_name TEXT,
       last_name TEXT
       )
    '''

    try:
        cur.execute(qry_create_table)
        print('Table created...')

    except sqlite3.Error as e:
        print(f'ERROR: Could not create table: {e}')
        exit(1)

    actors = (
        ('Chris', 'Farley'),
        ('David', 'Spade'),
        ('Keanu', 'Reeves'),
        ('Denzel', 'Washington'),
        ('Paul', 'Rudd'),
        ('Scarlett', 'Johanson'),
        ('Morgan', 'Freeman'),
        ('Evangeline', 'Lilly'), #Cassie Lang
        ('Nicholas', 'Cage'),
        ('Robert', 'Downey Jr.'),
        ('Chris', 'Hemsworth'),
        ('Brad', 'Pitt'),
        ('Angelina', 'Jolie'),
        ('Matt', 'Damon'),
        ('Rachel', 'McAdams'),
        ('Chris', 'Pratt'),
        ('John', 'Wayne'),
        ('Bradley', 'Cooper')
        )

    qry_insert_actors = 'INSERT INTO Actor (first_name, last_name) VALUES (?, ?)'
    try:
        cur.executemany(qry_insert_actors, actors)
        row_count = cur.rowcount
        print(f'Actors inserted... {row_count} rows')
        db.commit()

    except sqlite3.Error as e:
        print(f'ERROR: Data could not be inserted: {e}')
        exit(1)

    qry_row_count = 'SELECT COUNT(*) AS RecCnt FROM Actor'
    try:
        cur.execute(qry_row_count)
        count = cur.fetchone()[0]
        print(f'The current number of rows is: {count}')
    
    except sqlite3.Error as e:
        print(f'ERROR: Could not select the number of rows: {e}')
        exit(1)

    #More fun database stuff
    try:
        # Get column names via meta-data table_info. Super cool!!!
        qry_columns = 'PRAGMA table_info(Actor)'
        cur.execute(qry_columns)
        row = cur.fetchall()
        colnames = [r[1] for r in row]
        print(f'Column names include: {colnames}')

    except sqlite3.Error as e:
        print(f'ERROR: Column names could not be pulled: {e}')
        exit(1)

    # Look into 'yield' statement. Looping through rows

    # Even more goodies
    # use row_factory for tuple or dictionary results
    cur.execute("SELECT * FROM Actor")
    cur.row_factory = sqlite3.Row
    for row in cur:
        print(f"As tuple: {tuple(row)} -> As dict: id:{row['id']}, First:{row['first_name']}, Last:{row['last_name']}")

    # reset / clear row factory
    cur.row_factory = None

    cur.execute("SELECT MAX(id) FROM Actor")
    max_id = cur.fetchone()[0]
    #max_id = cur.fetchmany(5) # fetch 5 at a time
    print(f"The max id is: {max_id}")

    cur.execute("DROP TABLE IF EXISTS Actor")

    cur.close()
    db.close()

if __name__ == "__main__":
    main()


