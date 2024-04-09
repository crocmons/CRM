import pymysql

# Connect to MySQL server
database = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
)

# Create a cursor object
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE CRM_DB")

print("All done!")
