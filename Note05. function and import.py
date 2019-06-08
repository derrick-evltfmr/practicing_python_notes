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
