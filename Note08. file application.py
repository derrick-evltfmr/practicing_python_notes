# file application
# // with document file, we can save some record inside it and read the record from the file later to get some tasks done
# // however, if we just simple save the data in the text file, the data is just some string, it doesn't have any query function like in database
# // in Python, we can save the data in a list or dict like format, with specific packages, we can convert the text data into useful data that we can use

data = {"derrick":"123123", "john":"456456", "charles":"789789"}
with open('password.txt','w', encoding = 'UTF-8-sig') as f:
    f.write(data)                                                        # the data is dict, however, after written in the txt file, it is just simply string, not dict

# ast package and literal_eval() to convert string to list/dict
import ast                                                               # ast package (Abstract Syntax Tree)
data = dict()
with open('password.txt', 'r', encoding = 'UTF-8-sig') as f:
    filedata = f.read()                                                  # file read the string "{"derrick":"123123", "john":"456456", "charles":"789789"}"
    data = ast.literal_eval(filedata)                                    # using literal_eval() function in ast package to convert the string to list or dict
                                                                         # now data = {"derrick":"123123", "john":"456456", "charles":"789789"}

# >>> example of a simple Account/Password Management System using the file related functions (from the book)
import os
def menu():                                                              # [[Function]] display a menu for user to choose the option they need
    os.system("cls")
    print("Account Password Management System")
    print("----------------------------------")
    print("1. Enter account and password")
    print("2. display account and password")
    print("3. modify password")
    print("4. delete account and password")
    print("0. end program")
    print("----------------------------------")

def readData():                                                          # [[Function]] read in data from file
    with open('password.txt', 'r', encoding = 'UTF-8-sig') as f:
        filedata = f.read()                                              # read data from the file into filedata
        if filedata != "":                                               # if the filedata is not empty (the data read from the file is not empty)
            data = ast.literal_eval(filedata)                            # convert the filedata(string type) to data (dict type)
            return data                                                  # return data
        else: 
            return dict()                                                # if the filedata is empty, return empty dict

def displayData():                                                       # [[Function]] display the data (account and password) to the user
    print("Account\tPassword")                                           # \t is an escape character for tab
    print("=========================")
    for key in data:                                                     # data was converted to dict type by readData function
        print("{}\t{}".format(key,data[key]))                            # get key from the dict object, to print out the key, and use the key to access the data[key]
    input("Press any key to go back to the menu")

def inputData():
    while True:
        name = input("Please enter account: ")
        if name == "": break
        if name in data:                                                 # if the account name already existed, then not allow to enter
            print("Account {} already existed!".format(name))
            continue
        password = input("Please enter password")                        
        data[name]=password                                              # data[name], the value of data writes in the new password
        with open('password.txt', 'w', encoding = 'UTF-8-sig') as f:     # open the password.txt
            f.write(str(data))                                           # write the data(convert to str type) into the file ('password.txt')
        print("The password of {} has already saved.".format(name))      # display the password updated message

def editData():
    while True:
        name = input("Please enter the account you want to modified: ")
        if name == "": break
        if not name in data:
            print("Account {} does not exist ".format(name))             # if the Account does not exist, cannot edit the password
            continue
        print("The original password is: {}".format(data[name]))
        password=input("Please enter the new password: ")
        data[name] = password
        with open('password.txt', 'w', encoding = 'UTF-8-sig') as f:
            f.write(str(data))
            input("Password has already updated, please press any key to go back to menu")
            break

def deleteData():
    while True:
        name = input("Please enter the account you want to delete: ")
        if name == "": break
        if not name in data:
            print("Account {} does not exist".format(name))
            continue
        print("Confirm to delete the data of {}? :".format(name))
        reply = input("Y or N?")
        if (reply == "Y" or reply == "y"):
            del data[name]
            with open('password.txt', 'w', encoding = 'UTF-8-sig') as f:
                f.write(str(data))
                input("Data has already been deleted, please press any key to continue")
                break


# main program of the example

import os, ast
data = dict()

data = readData()                                                        # read in data(string) and convert into dict type
while True:
    menu()
    choice = int(input("Please enter your choice: "))
    print()
    if choice == 1:                                                      # ( ) of the condition are optional in Python
        inputData()
    elif choice == 2:
        displayData()
    elif choice == 3:
        editData()
    elif choice == 4:
        deleteData()
    else:
        break

print("The Program is finished.")

