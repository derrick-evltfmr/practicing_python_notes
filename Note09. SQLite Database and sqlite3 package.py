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


# >>> example: using a cursor to execute SQL command
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