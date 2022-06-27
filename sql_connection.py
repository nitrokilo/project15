import mysql.connector as my_sql
from mysql.connector import Error


def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = my_sql.connect(
            host=hostname,
            user=username,
            password=userpw,
            database=dbname
        )
        print("success")
    except my_sql.Error as e:
        print(f"the error '{e}' occured")
    return connection


# add parameters to "conn"
# conn = create_con("my-db.ccl4pqjiwtpl.us-east-2.rds.amazonaws.com","admin","Gold5400","test_table")
# cursor = conn.cursor(dictionary = True)
# sql = 'select * from users'
# cursor.execute(sql)
# rows = cursor.fetchall()
#
# for user in rows:
#   print(user)
#   print('first name is: ' + user['firstname'])

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed sucessfully")
    except Error as e:
        print(f"The error '{e}' occured")


def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
