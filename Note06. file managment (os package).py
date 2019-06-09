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

# - execute system commands (system())
# // just execute commands like the way you use cmd, but in str way, using " "
import os
current_path = os.path.dirname(__file__)                                 # os.path.dirname(file)          // get the directory path of the file
os.system("cls")                                                         # clear the screen
os.system("mkdir newdirectory")                                          # make a directory
os.system("copy myfile.txt newdirectory/copyfile.txt")                   # copy a file

copyfile = current_path + "/newdirectory/copyfile.txt"
os.system("notepad++ " + copyfile)                                       # open the file with notepad++


# os.path (part of the os package)
# // os.path can help to deal with the file path and name, to check whether the file or path exists, and calculate the size of the file
import os.path
someFile = "myfile.txt"
somePath = "C:/somedirectory/"
os.path.abspath(someFile)                                                # return the complete path of the file
os.path.dirname(someFile)                                                # return the complete path of the directory of the file
os.path.dirname(__file__)                                                # return the complete path of the directory of the current file (__file__)
os.path.exists(someFile)                                                 # check whether the file exists
os.path.getsize(someFile)                                                # get the size of the file

os.path.isabs(somePath)                                                  # check whether the path is a complete path
os.path.isfile(somePath)                                                 # check whether the path is a file
os.path.isdir(somePath)                                                  # check whether the path is a directory

os.path.split(somePath)                                                  # split the path to directory path and file
os.path.splitdrive(somePath)                                             # split the path to the drive and the file path
os.path.join(somePath + "/" + someFile)                                  # join/group the path and the file to a complete path        