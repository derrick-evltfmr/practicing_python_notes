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