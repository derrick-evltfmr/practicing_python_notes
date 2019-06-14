# SQLite Database
# // Although using text file to store the data is easy and simple, while we have high amount of data, it will be hard to handle the data
# // it will be hard to query and modify the data
# // in Python 3.x, there's a built-in database SQLite, which use one file (.sqlite) the store the whole database, it's convenient for those who need to deal with data
# // We can use the SQL language syntax to manage the database, to add, modify, delete or query

##### SQLite Manager (Chrome extension / Firefox plugin) #####
# // there's no built-in GUI tool in Python, but we can use a plugin from the browswer Chrome or Firefox - SQLite Manager
# // some basic tutorial for SQLite Manager (like Python, we don't need ; like the formal SQL syntax)

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
                                                                         #
