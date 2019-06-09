# os package
# // os package can help to create directory, delete directory, delete file, call system command, etc.

# - remove file (remove() and exists())
import os
file = "myfile.txt"
if os.path.exists(file):                                                 # os.path.exists(filename)       // check whether the file exists
    os.remove(file)                                                      # os.remove(filename)            // remove the file (it's usually used with os.path.exists() )
else:
    print(file + " does not exist!")