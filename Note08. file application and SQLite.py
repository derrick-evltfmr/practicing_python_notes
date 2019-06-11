# file application
# // with document file, we can save some record inside it and read the record from the file later to get some tasks done
# // however, if we just simple save the data in the text file, the data is just some string, it doesn't have any query function like in database
# // in Python, we can save the data in a list or dict like format, with specific packages, we can convert the text data into useful data that we can use

data = {"derrick":"123123", "john":"456456", "charles":"789789"}
with open('password.txt','w', encoding = 'UTF-8-sig') as f:
    f.write(data)                                                        # the data is dict, however, after written in the txt file, it is just simply string, not dict

