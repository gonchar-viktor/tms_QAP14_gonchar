import mysql.connector as mysql
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="qwerty@123"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE test_db")


# import mysql.connector as mysql
#
# print(mysql.connect(host="localhost",
#                     user="root",
#                     passwd="qwerty@123"))