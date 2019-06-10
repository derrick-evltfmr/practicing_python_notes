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
