# // in python, like array in C++ and ArrayList in Java. Python use List. (and also Tuple and Dict)

# list [ element1, element2, ... ]
list1 = [1, 2, 3, 4, 5, 6]         # like array, list in python can store elements in the same type
list2 = [True, 2.0, 3, "4", [5,6]] # but it can also store elements of different types, and also list element (tuple and dict elements) in the list

print(list1[1])    # 1
print(list2[5][1]) # 6
print(list1[-1])   # 6 (index can be negative in python, the last element is index -1 and counting back from the right)
print(len(list2))  # lenght of list2 is 5, because it is only counting the list elements, so [5.6] is count as one element only
list2[0] = False   # list is alterable

list3 = ["a", "b", "c"]
del list3          # delete a list with del keyword

# // if you think of list is an array that you can change the elements in it, then tuple is like a non-alterable list. (a constant/final list that cannot be changed in C++/Java concept)

# tuple ( element1, element2, ... )
tuple1 = (5, 4, 3, 2, 1, 0)
tuple2 = ("blue", "yellow", "orange")

print(tuple2[3])   # orange
print(len(tuple1)) # lenth of tuple1 is 6, tuple can also return len() just as list


# // tuple is safer and executes faster than list, but the tuple itself and its elements cannot be changed
# // a useful way is to convert list[] to tuple() and tuple() to list[], to achieve the purpose we want

# conversion between list and tuple (tuple() and list())
list3 = ["This is a password", "abcdefg", "I don't want the list to be altered"]
tuple3 = tuple(list3)  # now the elements in tuple3 cannot be revised

tuple4 = (2, 4, 6, 8, 10)
list4 = list(tuple4)
list4[3] = 12          # element value 8 now changed to 12
tuple4 = tuple(list4)  # now tuple4 is reassigned to (2, 4, 6, 12, 10)

del tuple4          # delete a tuple with del keyword


# // dict is a key, value pair, we can use the key to get the value in the dict

# dict { key1:value1, key2:value2, ... }
dict1 = {"blue":20, "yellow":30, "orange":60}
print(dict1["orange"]) # 60

dict2 = {"blue":20, "yellow":30, "orange":60, "blue":40}
print(dict2["blue"])   # 40  (if a key appear more than one time in the dict, the last appearance will replace the previous appearance(s))

dict2["red"] = 50      # we can add new key into the dict
del dict1["orange"]    # we can remove a key:value pair using the key

dict1.clear()          # this can remove all elements inside a dict
del dict1              # we can also use del keyword for deleting list, tuple, dict


# // range() can set up a list of numbers, which is used very frequent in a loop

# range() (keep in mind that in range() always end at endvalue - 1)
list5 = range(6)       # list5 = [0, 1, 2, 3, 4, 5], range(end-1), range(6) => index 0~5
list6 = range(-2,4)    # list6 = [-2, -1, 0, 1, 2, 3], range(start, end-1), range(-2,4) => index -2~3
list7 = range(3,8,2)   # list7 = [3, 5, 7], range(start, end-1, step), range(3,8,2) => index 3~7, step2 [[step default is 1]]
list8 = range(9,4)     # list8 = [9, 8, 7, 6, 5, 4], if start > end-1, the list is going in backward step [[step deafult backward is -1]]















 