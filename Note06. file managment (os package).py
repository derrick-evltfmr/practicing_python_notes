# os package
# // os package can help to create directory, delete directory, delete file, call system command, etc.

# - remove file (remove() and exists())
import os
file = "myfile.txt"
if os.path.exists(file):                                                 # os.path.exists(filename)       // check whether the file exists
    os.remove(file)                                                      # os.remove(filename)            // remove the file (it's usually used with os.path.exists() )
else:
    print(file + " does not exist!")

# - make directory (mkdir())
import os
os.mkdir("mydirectory")                                                  # os.mkdir(dirname)             // make a directory
# // HOWEVER, the way above is not enough in practice,
# // it's because if the directory is already existed, it will cause error while executing
# // so usually we need to check whether the directory exists, then decided to make the directory or not
dir = "mydirectory"
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print(dir + "exists already!")

# - remove directory (rmdir() and exists())
# // similar to remove file, we will check whether the directory exists first, then delete
import os 
dir = "mydirectory"
if os.path.exists(dir):                                                  # exists() can also use for directory
    os.rmdir(dir)                                                        # to remove a directory, we use rmdir(), not just remove()
else:
    print(dir + " does not exist!")


