# function in Python
# // in Python, we use 'def' to declare a function, and since in Python we don't need to specify datatype, so we don't have to put int, str... in the function declaration
def functionName(parameter1, parameter2, parameter3):
    print("I'm a block.")
    returnvalue1 = parameter1
    returnvalue2 = parameter2
    returnvalue3 = parameter3
    return returnvalue1, returnvalue2, returnvalue3                      # return is optional in a function

# - e.g. a function of converting Celsius to Fahrenheit
def CtoF(C):
    F = C * 1.8 + 32
    return F

input = float(input("Please enter the Celcius Degree: "))
print("Fahrenheit Degree is: %5.1f" % CtoF(input))


# default values of the parameters
# // in a function, sometimes for some value we don't have it everytime and we want it to be optional (and have a default value)
# // e.g. def function (parameter1, parameter2) , of course we can call function(var1, var2) by 2 parameteres, but in some case, we may not have var2
# // we want var2 to be some default value, so we can just call function(var1) with 1 parameter, and the var2 value was set as some default value
# // note that we can only have the default value in the end of the parameter list
def GetArea(width, height=12):
    return width * height
Rectangle1 = GetArea(6)                                                 # Rectangle1 = 72 (6 * 12) // since we don't have height in the parameter, it use the default
Rectangle1 = GetArea(6, 9)                                              # Rectangle1 = 72 (6 * 9)  // since there is height in parameter, we use the parameter directly

# def GetArea(width=18, height):                                        # Note that this is not correct, if we want to set width=18 as default,
                                                                        # we need to move it to the end


# uncertain amount parameters in a function
# // in many functions, we know how many parameters we need for the function
def add(n1, n2):
    return n1+n2
result = add(10,20)                                                    # 30 // we know the add function has only 2 parameters

# // However, what if we want to add more than 2 variables? the add function above will not work because it only accepts 2 parameters
# // in python, we can accept multiple, uncertain amount of parameters as follows:
def sum(*parameters):
    total = 0
    for param in parameters:
        total += param
    return total

print("result = %d" % sum(10,20))                                     # result = 30
print("result = %d" % sum(10,20,30))                                  # result = 60
print("result = %d" % sum(10,20,30,40))                               # result = 100


# global and local variable in Python
# // like in C++ or Java, if we want a variable to be valid in all over the program, we set it up (declare it) outside the functions
# // and when we want the variable only exist in a specific scope, we put it inside the function or scope
# // while in Python, we have a way to declare the global variable inside the functions, by using 'global' keyword
def scope():
    global var1
    var1 = 1
    var2 = 2
    print(var1, var2, end = '')                                       # 1 2

var1 = 10
var2 = 20
scope()
print(var1, var2, end = ' ')                                          # 1 20


# built-in functions in Python (not exhaustive listed)
# - type conversion
int("56")                                                             # 56        // to int
float(56)                                                             # 56.0      // to float
str(56)                                                               # "56"      // to str

# - character conversion
chr(65)                                                               # "A"       // to the char of the unicode value  [ Note that it's 'chr', not 'char' ] 
ord("A")                                                              # 65        // to unicode value of the char [ord stand for ordinal]

# - Maths related
abs(-1)                                                               # 1         // absolute value
divmod(50, 8)                                                         # (6,2)     // tuple of (quotient, remainder)
max(1,3,5,7)                                                          # 7         // max and min are not limited in list, so it can be multiple parameters
min(1,3,5,7)                                                          # 1         // min in the parameters
pow(2,3)                                                              # 8         // pow(base,power)
round(45.8)                                                           # 46        // rounding with one parameter, to integer by default (<4 decrease, >6 increase, 5 if previous digit even decrease [IMPORTANT]
                                                                      #                                                                                              if previous digit odd increase  [IMPORTANT])
round(1.23, 1)                                                        # 1.2       // rounding with two parameters, the 2nd parameter is to tell how many numbers after the decimal point you want to keep
round(1.25361, 3)                                                     # 1.254     // after decimal point . , 3 numbers were kept
round(1627731, -3)                                                    # 1628000   // the 2nd parameter can be negative, how many 0 before the decimal point you want to have

round(3.65, 1)                                                        # 3.6       // mentioned in the note above, if the digit you want to round is 5, if the previous digit even, decrease. 
round(3.75, 1)                                                        # 3.8       // if the previous digit odd, increase. This is the change from Python 3.x, it's for the reason of accuracy
                                                                      #              since the original method there are 4 numbers 0~4 to decrease, but 5 numbers 5~9 to increase, bias will exist
                                                                      #              IF WE REALLY WANT TO DECREASE WHEN 0~4 AND INCREASE WHEN 5~9, WE NEED TO WRITE OUR OWN FUNCTION FOR THAT

# - Positional notation
bin(79)                                                               # 0b1001111 // binary number
oct(34)                                                               # 0o42      // octal number
hex(34)                                                               # 0x22      // heximal number

int(11001,2)                                                          # 25        // to integer number (number, base), so in this example, 11001 in base2 (binary) to decimal integer

# - List (tuple/dict) related                                         # (Please see Note03 for more details)
len([1,3,5,7])                                                        # 4         // length of the list (number of elements)
max([1,3,5,7])                                                        # 7         // max in the list
min([1,3,5,7])                                                        # 1         // min in the list
sum([1,3,5,7])                                                        # 16        // sum of the list elements
sorted([3,1,7,5])                                                     # [1,3,5,7] // return sorted list (ascending order)


# import
# // There are numerous packages(or called modules) can be used in Python, they can help the developers to achieve various powerful functions without typing the code line by line
# // Although import is simple, there're still some details needed to be paid attention to

import random                                                         # random is a package to generate random numbers
random.seed()                                                         # there are functions like seed(), random(), choice() inside...

from random import *                                                  # However, repeating the package name again and again can be tiring
seed()                                                                # using from import syntax, we can just call the functions without typing the package name
                                                                      # there's one downside that you may not know every functions in the package, if you import all of them
                                                                      # for example, you want to declare a function setstate, but you already have the import function named setstate,
                                                                      # then they will have conflict

from random import seed, random, choice                               # with this way, we can import seed, random, choice only from random package
seed()                                                          

import random as r                                                    # there's also a useful way, to rename the import package
r.seed()                                                              # by doing this, we don't have to repeat the full package name all the time, and also can avoid having the same function names







