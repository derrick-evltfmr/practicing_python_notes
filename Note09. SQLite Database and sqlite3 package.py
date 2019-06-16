# SQLite Database
# // Although using text file to store the data is easy and simple, while we have high amount of data, it will be hard to handle the data
# // it will be hard to query and modify the data
# // in Python 3.x, there's a built-in database SQLite, which use one file (.sqlite) the store the whole database, it's convenient for those who need to deal with data
# // We can use the SQL language syntax to manage the database, to add, modify, delete or query

##### SQLite Manager (Chrome extension / Firefox plugin) #####
# // there's no built-in GUI tool in Python, but we can use a plugin from the browswer Chrome or Firefox - SQLite Manager
# // some basic example for using SQLite Manager (like Python, we don't need ; like the formal SQL syntax)

# db_new("SQLite01.sqlite")                                              // to create a new sqlite Database file named SQLite01 (we can also find the syntax from the top 
#                                                                               bar to call the dropdown list, to create the database file   ) 

# CREATE TABLE password(                                                 // create a table named password
#  name VARCHAR PRIMARY KEY,                                                    the table has an attribute name, which is the Primary Key
#  pass VARCHAR                                                                 the table has an attribute pass
# )


# INSERT INTO password(name,pass)                                        // insert into the table(col1,col2...)
#  VALUES('Derrick','123123'),                                                  insert 'Derrick' in name column, insert '123123' in pass column (this is one row) 
#        ('Alex','456456'),                                                     One thing needs to pay attention to is, the values need to fit the table column type
#        ('Stephen','789789')                                                   therefore, name and pass are VARCHAR type, we must put the '' or ""
#                                                                               otherwise, they're not VARCHAR values and will lead to an error

# // other SQL syntax please refer to other SQL references, above are just some simple example

###############################################################


# sqlite3 package
# // To use a database, we need to build the connection between Python and the database
# // we can use sqlite3 package

import sqlite3                                                           # import sqlite3 pacakage
connection = sqlite3.connect('SQLite01.sqlite')                          # build the connection with the .sqlite database file
connection.close()                                                       # close the connection after finish

### connection object has the following methods:
connection.cursor()                                                      # create a cursor object, with the execute method, the cursor can do the actions in execute() method
connection.execute('CREATE TABLE hello_world')                           # to execute SQL command(string type), can do the actions of create table, add, modify, delete and query
connection.commit()                                                      # to commit, to make the database updated
connection.close()                                                       # close the connection


### using a cursor to execute SQL command
import sqlite3
connection = sqlite3.connect('test.sqlite')
cursor = connection.cursor()
                                                                         # SQL command string, it's better to use ' ' to indicate the beginning and end of string in SQL
sqlstr = "CREATE TABLE IF NOT EXISTS table01 \
          ('num' INTEGER PRIMARY KEY NOT NULL, 'tel' TEXT)"
                                                                         # we use \ to define the string still continue on the next line
cursor.execute(sqlstr)                                                   # execute the SQL above

sqlstr = "INSERT INTO table01 VALUES(1, '0-123-456-789')"

cursor.execute(sqlstr)

connection.commit()                                                      # commit in the SQL
connection.close()                                                       # close the connection


### using connection to execute SQL command directly
import sqlite3
connect = sqlite3.connect('test.sqlite')

num=1
tel="312-456-7890"
sqlstr = "INSERT INTO table01 values({}, '{}')".format(num,tel)
connect.execute(sqlstr)                                                  # call execute() from connection object
connect.commit()

sqlstr = "UPDATE table01 SET tel = '{}' where num = {}".format("012-345-6789",1)
connect.execute(sqlstr)
connect.commit()

sqlstr = "DELETE FROM table01 where num = 1"
connect.execute(sqlstr)
connect.commit()

sqlstr = "DROP TABLE table01"
connect.execute(sqlstr)
connect.commit()

connect.close()


# cursor: use cursor to query data
# // after using execute() a SQL query command called from connection object, it will return a cursor object, which can be used to query data
cursor = connect.execute("SELECT * FROM table01")                        # after executing the SQL commands, the data from the command will be indicated by the cursor

# there are two methods can be used in a cursor object
cursor.fetchall()                                                        # using a 2D list (similar to 2D array) to store all the data matched the query condition
cursor.fetchone()                                                        # using a list to store the first record of the data
                                                                         # if fetchall() or fetchone() finds no record from the query condition, it will return [[None]]

# >>> example of using cursor to query data (fetch all data)
import sqlite3
connect = sqlite3.connect('test.sqlite')
cursor = connect.execute("SELECT * FROM table01")
rows = cursor.fetchall()
print(rows)                                                              # e.g. [(1, '312-456-7890'), (2, '012-345-6789)]     // inside the list, each record is a tuple
for row in rows:                                                         # e.g. row[0] and row[1] means the first and second elements in the row
    print("{}\t{}".format(row[0], row[1]))                               #
                                                                         #      1   312-456-7890                              // with for loop and string format
                                                                         #      2   012-345-6789                              // we can get each record from fetchall()


# >>> example of using cursor to query data (fetch one record (the first one))
cursor = connect.execute("SELECT * FROM table01 WHERE num=1")
row = cursor.fetchone()
if not row == None:                                                      # if the result is not None
    print("{}\t{}".format(row[0], row[1]))                               # print the record of fetchone()
                                                                         #      1   312-456-7890


# >>> example of a simple Account/Password Management System using SQLite (the example from Note08)

import os
import sqlite3

connect = sqlite3.connect('Sqlite01.sqlite')

sqlstr = "CREATE TABLE password(\
            name VARCHAR PRIMARY KEY,\
            pass VARCHAR\
         )"

connect.execute(sqlstr)

sqlstr = "INSERT INTO password(name,pass)\
            VALUES('derrick','123123'),\
            ('john','456456'),\
            ('charles','789789')"

connect.execute(sqlstr)
connect.commit()


def menu():                                                              # [[Function]] display a menu for user to choose the option they need (same as Note08)
    os.system("cls")
    print("Account Password Management System")
    print("----------------------------------")
    print("1. Enter account and password")
    print("2. display account and password")
    print("3. modify password")
    print("4. delete account and password")
    print("0. end program")
    print("----------------------------------")

#############################################################################
# // we don't need readData because we don't read the data from the text file
#############################################################################

def displayData():                                                       # [[Function]] display the data (account and password) to the user (modified to use cursor)
    cursor = connect.execute("SELECT * FROM password")

    print("Account\tPassword")                                           
    print("=========================")
    for row in cursor:                                                   # changed from for key in data to for row in cursor
        print("{}\t{}".format(row[0], row[1]))                           # account is row[0] (first element of the row, password is row[1] (2nd element of the row)
    input("Press any key to go back to the menu")

def inputData():
    while True:
        name = input("Please enter account: ")
        if name == "": break
        
        sqlstr = "SELECT * FROM password where name = '{}'".format(name)

        cursor = connect.execute(sqlstr)
        row = cursor.fetchone()

        if not row == None:
            print("Account {} already existed!".format(name))
            continue

        password = input("Please enter password")       

        sqlstr = "INSERT INTO password \
                    VALUES('{}','{}')".format(name, password)

        connect.execute(sqlstr)                                          # SELECT SQL command we have the return cursor, but other commands like INSERT we just execute it
        connect.commit()                                                 # after making some changes, commit()

        print("The password of {} has already saved.".format(name))      # display the password updated message
