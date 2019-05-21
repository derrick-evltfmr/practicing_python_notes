# // in python, no ; in the end of the statement, using # to write a comment


# declaration (doesn't have to declare the type) and operators 
var1 = 2**4        # ** operator: base**power
var2 = 14/4        # / for normal division, has numbers after decimal point 14/4=3.5
                   # // operator: integer divison 14//4 = 3
                   # %=, //=, **=, assignment operators
var3 = "abcdefg"   # "" or ''
var4 = True


# logical operators (and, or, not)
varAnd = (5>3) and (9>6) # True   # & Bitwise AND
varOr  = (5<3) or  (9<6) # False  # | Bitwise OR
varNot =       not (5>3) # False  # ~ Bitwise NOT


# print
print(var1,var2,var3,var4)                                             # print variable values (in separate lines [in default end char is "\n"])
print(var1,var2,var3,var4,sep="&",end="")                              # print variable values (using & to separate each of them, and print in the same line)
print("var1 %d var2 %f var3 %s var4 %r" % (var1, var2, var3, var4))    # print using %, d=decimal(int), f=float, s=string, r=__repr__ (or use %s for boolean)
                                                                       #    %5d   (if less than 5 numbers, fill to 5 character space on the left e.g. "   16")
                                                                       #    %-5d  (if less than 5 numbers, fill to 5 character space on the right e.g. "16   ")
                                                                       #    %8.2f (total 8 character space(include dec pt), front.back = 5space.2space e.g. "    3.50" )
print("var1 {} var2 {} var3 {} var4 {}".format(var1,var2,var3,var4))   # print using {} and .format


# type()
print(type(var1))  # <class 'int'>
print(type(var3))  # <class 'str'>
print(type(var4))  # <class 'bool'>


# type conversion
str(var1)          # to str
float(var1)        # to float
int(var1)          # to int


# input
score = input("Please enter the student's final exam score: ")         # input("hint text for the input") [[hint text is optional]]


# del (variable)
garbageVariable = "hfih2r23oj23oj32j25o2352420fu09fwufwfw"
del garbageVariable                                                    # in python, we use del keyword to delete variable, and also other things like list, tuple, dict ....








 