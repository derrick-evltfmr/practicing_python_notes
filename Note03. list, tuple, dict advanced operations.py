# list

# - initializing a list using an existing list
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = list1[1:4:2]                   # list2 = [1.3]  // list1 index 1 to 4-1, step = 2   

# - append() and extend()  (adding the elements in the end of the list)
list3 = [0, 1, 2, 3, 4, 5, 6]
list4 = [7, 8 ,9]

list3_append = list3.append(list4)     # [0, 1, 2, 3, 4, 5, 6, [7, 8, 9] ]      // append will add ONE  element, even though it is a list, it will add the list as ONE element [7, 8, 9]
list3_extend = list3.extend(list4)     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]         // extend will add EACH element of the list into the list we want to add, it will add three element 7, 8, 9

# - properties function of list (not exhaustive)
n = len(list1)                         # length is 10
n = min(list1)                         # min is 0
n = max(list1)                         # max is 9

list5 = [1, 9, 5, 3, 15, 25, 100, 30]
list5.sort()                           # [1, 3, 5, 9, 15, 25, 30, 100]
list5.reverse()                        # [100, 30, 25, 15, 9, 5, 3, 1]

list6 = [1, 1, 2, 3, 5, 8, 13, 21, 34]
n = list6.index(21)                    # index 8         // the first appearance of 21 in the list
n = list6.count(1)                     # counted 2 times // how many times the element 1 appears in the list

# - insert and remove element
list7 = [1, 3, 5, 7, 9, 11, 13, 15]
var1 = 6

list7.append(17)                       # [1, 3, 5, 7, 9, 11, 13, 15, 17]         // append an element at the end of the list
list7.insert(3, var1)                  # [1, 3, 5, 6, 7, 9, 11, 13, 15, 17]      // insert an element at a specific location of the list

list7.pop()                            # [1, 3, 5, 6, 7, 9, 11, 13, 15]          // pop remove an element at the end of the list
list7.pop(3)                           # [1, 3, 5, 7, 9 , 11, 13, 15]            // pop with the index parameter remove the element at the specific index location (index, not value)

list7_2 = [1, 15, 5, 5, 3, 7, 9, 13]
list7_2.remove(5)                      # [1, 15, 5, 3, 7, 9, 13]                // remove the first appearance of the element 5 (value, not index) in the list


# tuple

# - tuple can do nearly the same as list, but note that a tuple cannot be revised
#   therefore it's ok to call the following functions to get the properties of the tuple
tuple1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) 
n = len(tuple1)                        # length is 10
n = min(tuple1)                        # min is 0
n = max(tuple1)                        # max is 9

n = tuple1.index(5)                    # index 6         // the first appearance of 6 in the tuple
n = tuple1.count(5)                    # counted 1 time  // how many times the element 5 appears in the list

# - since a tuple is a non-alterable list, we cannot use append(), insert(), pop(), sort(), reverse(), etc.
#   if we really want to change the value of a tuple, we can use the way introduced in Note02, to convert a tuple to a list, change the value and convert it back to a tuple
list_tuple1 = list(tuple1)
list_tuple1[6] = 555
tuple1 = tuple(list_tuple1)            # (0, 1, 2, 3, 4, 555, 6, 7, 8, 9)       // reassign back to tuple1


# dict

dict1 = {"banana":2, "avocado":3, "apple":1}

# - add and remove items in the dict
dict1["strawberry"] = 3                # // like introdcued in Note02, dict can just add a key:value pair by assign dict[key] = value
del dict1["strawberry"]                # // and delete a key:value pair by the key

# - copy and remove elements of/delete the dict
dict2 = dict1.copy()                   # // make a copy of the dict1
dict1.clear()                          # // now dict1 is an empty dict
del dict1                              # // now dict1 is deleted

# - properties functions of dict (not exhaustive)
n = len(dict2)                         # lenth is 3                                            // 3 elements(key:value pairs)
n = "apple" in dict2                   # True                                                  // key in dict is a boolean, it will return True / False to check whether the key exists in the dict

# - getting the set of the key:value pairs/ keys/ values in the dict
dict3 = dict2.items()                  # dict3 = [("banana":2), ("avocado":3), ("apple":1)]    // list all key:value pairs in the dict (note that key:value pairs are tuple elements)
dict3 = dict2.keys()                   # dict3 = ["banana", "avocado", "apple":1]              // list all keys in the dict
dict3 = dict2.values()                 # dict3 = [2, 3, 1]                                     // list all values in the dict
# // note that dict3 actually is not a dict type, in python, we don't have to bind a var with a fixed type
# // therefore dict3 is just a variable with the name dict3, it can assign anything to it. e.g. dict3 = "abc"
# // dict3 above is indeed in dict_items, dict_keys, dict_values type.
# // but these types are just the same as list type, we can use list( ) to convert it into a list, so that we can use the result of dict.items(), dict.keys(), dict.values()
list_dict2items  = list(dict2.items()) 
list_dict2keys   = list(dict2.keys())
list_dict2values = list(dict2.values())   

# - get() and setdefault() (return the value of the key)
n = dict2.get("avocado")               # n = 3
n = dict2.setdefault("avocado")        # n = 3
# // if the key:value pair exists, get() and setdefault() will get the same,
# // however, they perform differntly when the key doesn't exist
n = dict2.get("strawberry",999)        # n = 999   // if the key doesn't exist in the dict, return the given value
                                       #           // dict2 = {"banana":2, "avocado":3, "apple":1}                     // strawberry not exist in dict, it's just returning a value
n = dict2.setdefault("strawberry",999) # n = 999   // if the key doesn't exist in the dict, ADD the key and the given value PAIR INTO THE DICT and return the value
                                       #           // dict2 = {"banana":2, "avocado":3, "apple":1, "strawberry":999}   // strawberry exist in dict now, it has set the default of strawberry to 999

# // since the value parameter is optional, we don't have to put a default value inside get() or default(), then what happen if we don't give it a default value but it doesn't exist?
dict3 = dict2.copy()
n = dict2.get("strawberry")            # n = None  // if the key doesn't exist in the dict, return None because there's no default value
                                       #           // dict2 = {"banana":2, "avocado":3, "apple":1}                     // strawberry not exist in dict, it's just returning a value
n = dict2.setdefault("strawberry")     # n = None  // if the key doesn't exist in the dict, ADD the key and the None PAIR INTO THE DICT and return None because there's no default value
                                       #           // dict2 = {"banana":2, "avocado":3, "apple":1, "strawberry":None}  // strawberry exist in dict now, it has set the default of strawberry to None
# // in some practical case, programmar may want to return the value if found, and return -1 when not found
# // we can add -1 as given value (or "not_found" as given value, because in a python, a list, tuple, dict can be mixed and mutli-type)
n = dict3.get("strawberry", -1)
n = dict3.setdefault("strawberry", -1)


