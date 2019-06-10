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

########################################################################################################################################################
### ONE THING THAT NEEDS TO PAY ATTENTION TO IS THAT, IN WINDOWS, IT USE '\' (backward slash), while other OS use '/' (forward slash)
### it seems that Python on Windows can also understand '/', so I just use '/' here
### but if we want to use '\', we need to be careful whether it is meaning the thing we want
### e.g. 
path = "C:\newDirectory"                                                 # this is not OK, it is because \n means new line, \t means tab and etc.
### therefore we need to use an escape character '\\' to tell the interpreter that it's not an esacpe character
path = "C:\\newDirectory"                                                # now this is correct
### alternatively, we can use raw string, which is much more convenient
path = r"C:\newDirectory"                                                # we define the string as raw string by simply adding a r before the quotes ""
########################################################################################################################################################

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


# os.walk
# // os.walk can search within specific directory and its sub directory, and return a 3-element tuple (Dir, SubDir, FileName)
import os 
current_path = os.path.dirname(__file__)                                 # get the current path
sample_tree = os.walk(current_path)                                      # os.walk can return the 3-element tuple (Dir, SubDir, FileName)
for dirname, subdir, files in sample_tree:
    print("File Path: ", dirname)                                        # Dir
    print("Dir List: ", subdir)                                          # SubDir
    print("File List: ", files)                                          # FileName
    print()


# shutil package
# // shutil is a more powerful file management package than os package, still, it supports cross-platform. 
import shutil
sourceFile = "sourceFile.txt"
destinationFile = "destinationFile.txt"
sourceDir = "C:/sourceDir"
destinationDir = "C:/destinationDir"
someDir = "C:/someDir"

shutil.copy(sourceFile, destinationFile)                                 # copy(srcFile, dstFile)         // copy src file to dst file
shutil.copytree(sourceDir, destinationDir)                               # copytree(srcDir, dstDir)       // copy src dir to dst dir (tree)
shutil.rmtree(someDir)                                                   # rmtree(dir)                    // delete dir directory and all the file inside
shutil.move(sourceFile, destinationFile)                                 # move(srcFile, dstFile)         // move src File/Dir 
shutil.move(sourceDir, destinationDir)                                   #      srcDir , dstDir                to dst File/Dir

# >>> example
import os, shutil
current_path = os.path.dirname(__file__)                                 # get the current path
destinationFile = current_path + "/" + "newfile.py"
shutil.copy("shutil.py", destinationFile)                                # copyfile from one file to another file path


# glob package
# // glob package can help to get the file List that matches specific condition(s)
# // the syntax is glob.glob("Path name")
# // The Path name can use * 
import glob
files = glob.glob("glob.py") + glob.glob("os*.py") + glob.glob("*.txt") # glob.glob("glob.py")            // return the list that the files matching "glob.py", e.g. glob.py (only)
for file in files:                                                      # glob.glob("os*.py")             // return the list that the files matching "os..... .py", e.g. osmkdir.py, ospath.py, osremove.py
    print(file)                                                         #                                                                                                osrmdir.py, ossytem.py
                                                                        # glob.glob("*.txt")             // return the list that the files matching "... .txt", e.g. A.txt, file1.txt, filetest.txt,fileUTF8.txt
                                                                        #                                                                                            memo.txt, password.txt


