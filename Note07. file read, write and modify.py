# open()
# // in Python, we can use the built-in function open() to open a specific file, to read, write or modify it
filename = 'text.txt'
mode = 'r'
encode = 'cp950'

### syntax of open()
open(filename, mode, encoding = encode)                                  # only filename is necessary, others are optional, there are 8 parameters in open(), usually we use filename, mode and encoding
                                                                         # filename can be relative path or absolute path, if there's no path specified, only the filename, then default is the current folder

### mode
mode = 'r'                                                               # read mode, which is the default mode when without the parameter
mode = 'w'                                                               # write mode, if the file exists, the content will OVERWRITE the original one
mode = 'a'                                                               # append mode, if the file exists, the content will add to the end of the original one


# >>> example (write a file):                                            # in Python, we can use """   """ or '''   ''' to define a multi-line string 
content = """
Hello Python 
This is the Note07 of my python self learning 
"""

myFile = open('myfile.txt', 'w')
myFile.write(content)
myFile.close()                                                          # Normally after we open a file, we should close the file

# >>> example (read a file):
myFile = open('myfile.txt', 'r')
for line in myFile:
    print(line, end = "")
myFile.close()

# with statement
# // usually after we open a file, we close it. But with with statement, then we don't need to call file.close(), it will close automatically
with open('myfile.txt','r') as myFile:
    for line in myFile:
        print(line, end = "")


# encoding
# // we can set the encoding format for the files
# // to find out the current operating system setting for encoding, we can use locale package as follows:
import locale
print(locale.getpreferredencoding())

# // in Europe an US Windows, the default encoding should be cp1252(ANSI), and for Traditional Chinese (Hong Kong, Taiwan) Windows, the default encoding is cp950(ANSI)
# // but Linux system uses UTF-8, so if we use cp950 to read UTF-8 file, we will get an error message (UnicodeDecodeError)
# // since many Linux system and international system are using UTF-8, it's suggested to save the files as UTF-8 rather than ANSI format



# commonly used functions for files
myFile = open('myfile.txt', 'w')
readsize = 5
########################################################################

myFile.readable()                                                       # check whether the file can be read
myFile.read()                                                           # read all the characters from the file
myFile.read(readsize)                                                   # read the specific size of characters from the file (e.g. readsize = 5, read 5 characters)
myFile.readline()                                                       # read the whole current line (including \n character)
myFile.readline(readsize)                                               # read the specific size of characters from the current line (e.g. readsize = 5, from the line)
myFile.readlines()                                                      # read all the lines from the file, and return as a list
myFile.next()                                                           # move to the next line
myFile.seek(0)                                                          # move to the beginning of the stream (file)
myFile.tell()                                                           # return the current position in the document

myFile.writable()                                                       # check whether the file can be written
myFile.write(content)                                                   # write the specific string into the document

myFile.flush()                                                          # when the file closes, it will write the data into the file, but we can also use flush() to force                                                                        # the data in the buffer zone to be written into the file instantly
myFile.close()                                                          # after the file closes, it can no longer do read and write actions


# BOM character (important to know)
### // this's important because it can cause big errors if the data is read in incorrectly !!! ###

# // see the following example, readlines() can return all the content in the document, including the hidden characters
# > write the file first
test = open('test.txt','w', encoding='UTF-8')
content = """
Hello Python 
"""
test.write(content)
test.close()

# > read the file above
with open('test.txt', 'r', encoding = 'UTF-8') as f:
    doc = f.readlines()
    print(doc)                                                          # \ufeffHello Python

f = open('text.txt', 'r', encoding ='UTF-8')
str1=f.read(5)
print(str1)                                                             # Hell
f.close()

# // reading in the file for 5 characters, shouldn't it print out "Hello", not "Hell"?
# // it's because in readlines(), we can see there's a character \ufeff, it is called the BOM character and it's generated automatically when using UTF-8 format
# // and it will occupy 1 character, therefore, '\ufeff' is the 1st character, and "Hell" are the 2nd to 5th character
# // this's important because it can cause big errors if the data is read in incorrectly !!! #

# // with some document editor like NotePad++, we can choose "Encode in UTF-8 (no BOM in the beginning)" to remove BOM character

# // Another very useful way is to add '-sig' after 'UTF-8' when reading in a file
with open('test.txt', 'r', encoding = 'UTF-8-sig') as f:
    doc = f.readlines()
    print(doc)                                                          # Hello Python

# // with this way, using 'UTF-8-sig', we can read in the files without the BOM character
