# // in C++ or Java, we use { } to show a block
# // but in Python, we use : and indentation(1 tab / 4 space) to distinguish a block

# if
if (1+1==2):                                                             # in EACH block, use : and indentation to show it is a block
    print("Your math is good")
else:
    print("It seems you have to spend more effort on studying math")

price = input("please insert the price of the item")
if (price>100):
    print("You've got 20% discount, the price is {}".format(price*0.8))
elif (price>50):                                                         # the only difference in if conditional is that [[ else if ]] spelled as [[ elif ]] 
    print("You've got 10% discount, the price is {}".format(price*0.9))
else:
    print("The price is {}".format(price))


# while 
total = n = 0
while (n<10):                                                           # use : and indentation to define a block
    n+=1                                                                # Python doesn't support ++, remember to use +=1
    total +=n
print(total)


# // if and while is nearly the same as in C++ and Java, the only things different are using : and indentation, and use [[ elif ]] insteade of [[ else if ]]
# // but in for loop, there're more things need to pay attention to

# for

# ( using range() )

n = 0
for i in range(1,101):                                                 # in C++ and Java, we use for(start_cond:end_cond:increment)
    for j in range(1,101):                                             # in Python, we use range() a lot, which introduced in Note02.
        n +=1                                                          # Note that range(start,end+1,[step]), we need to put end+1, and it will stop at end
print(n)                                                               # e.g. range(1,101) means 1 to 100, i 100times, j 100 times, therefore n = 10000


for i in range(1,31,2):                                                # for 1 to 30, step2(increment 2, like i+=2 in C++,java)
    print(i, end=" ")


# ( using list )
# // combine advance usage of dict
studentScore = {"John":100, "Harry":54, "Queenie":87 }

# way 1 to print the student score in the dict (using range(len(list)))
listkey = list(studentScore.keys())                                    # list of Name
listvalue = list(studentScore.values())                                # list of Score
for i in range(len(listkey)):                                          # range(len(list)), e.g. range(3), index 0 to 2
    print("%s 's score is %d"%(listkey[i], listvalue[i]))

# way 2 to print the student score in the dict (using variables in list)
listitem = list(studentScore.items())
for name, score in listitem:                                           # define the variables as name, score in the listitem
    print("%s 's score is %d"%(name, score))


# for else (usually comes with if and break)                           # there's no for else in C++/Java, but in Python,  we use for... else... to find out whether
                                                                       # the for loop completed running all iterations, or break out from the loop before the loop normally ended

n = int(input("Please insert an integer that is greater than 1"))
if (n==2):
    print("2 is a prime number")
else:
    for i in range(2,n):
        if (n%i == 0):                                                 # if the number can be fully divided by the divisor(smaller than the number itself) 
            print("%d is not a prime number" % n)                      # then it is not a prime number
            break                                                      # break the for loop, in this case, it will skip the else block of [[ for...else...]]
    else:
        print("%d is a prime number")                                  # only when the for loop tested all the iteration, and cannot find any divisor that can fully divide the number
                                                                       # e.g. 7, 7 divides by i (2 / 3 / 4 / 5 / 6), there's no 7 % i == 0, so it didn't break out
                                                                       # now the for loop is completed running all the iteration without breaking out
                                                                       # then it will run this else block
                                                                       # otherwise, i.e. if the for loop end by [[ break ]], it WON'T run this else block


# break and continue                                                   # same as C++ and Java

for i in range(1,11):
    if (i == 4): continue                                              # continue, if True, skip this iteration
    print(i, end=", ")                                                           
    if (i == 8): break                                                 # break, if True, end this loop

                                                                       # print result: 1, 2, 3, 5, 6, 7, 8, (because it use ", " to end instead of the default"\n"



