# DNS (Domain Name Resolution)
# // before acquring the data of a website, we need to know how the URL is constructed


# - urlparse() function from urllib package
# // we can use urlparse() to anaylise the url, and it will return a ParseResult object

# the properties of the ParseResult object are as follows:
# scheme    (index0)    // return the scheme communication protocol (return empty string if not exists)
# netloc    (index1)    // return the name of the website           (return empty string if not exists)
# path      (index2)    // return the path                          (return empty string if not exists)
# params    (index3)    // return the query parameters params str   (return empty string if not exists)
# query     (index4)    // return the query string (param of GET)   (return empty string if not exists)
# fragment  (index5)    // return the frame(fragment) name          (return empty string if not exists)
# port      (no index)  // return the port                          (return None if not exists)

# >>> example:
from urllib.parse import urlparse                                           # import urlparse() from urllib package
url = "http://thisisjustanexampleforDNS.com/webscraping/test.aspx?page=1"   # [!!!] This is a FAKE URL that's just used for explaination purpose [!!!]
parseObj = urlparse(url)
print(parseObj)                                                             # ParseResult(scheme='http', netloc='thisisjustanexampleforDNS.com:80', 
                                                                            #   path='/webscraping/test.aspx', params='', query='page=1', fragment='')                                                                   
print(parseObj.scheme)                                                      # http
print(parseObj.netloc)                                                      # thisisjustanexampleforDNS.com:80
print(parseObj.port)                                                        # 80
print(parseObj.path)                                                        # /webscraping/test.aspx
print(parseObj.query)                                                       # page=1


# - requests package (better than the built-in urllib pacakage)
# // we can use requests to read the souce code of a webpage
# // since it's better than urllib, so we can just use requests to replace it
# // we need to install the requests package (if you have installed the Anaconda IDE(integrated developing environment), than requests package is included)

import requests
url = "http://books.toscrape.com/"
html = requests.get(url)
html.encoding = "utf-8"
print(html.text)                                                            # this is the source code of the webpage that read from utf-8 encoding format

htmllist = html.text.splitlines()                                           # However, the way above includes the new line characters
for row in htmllist:                                                        # by using splitlines(), we can split the source code into rows without new line characters
    print(row)

### find the specific string from the source code
# // we can use 'in' or regular expression(regex) to query the data that matched
# // since text property is indeed a very long text string, we can use in to search for the words we want

import requests
url = "http://books.toscrape.com/"
html = requests.get(url)
html.encoding = "utf-8"

htmllist = html.text.splitlines()

n = 0                                                                       # initialize a variable to keep track of the times we found the word
word = "In Stock"

for row in htmllist:
    if word in row: n+=1                                                    # if found, n+=1
print("The word 'In Stock' appeared {} time(s)".format(n))

### if we want to use 'in' to search in string with case insensitive
htmllistUpper = htmllist.upper()

for row in htmllistUpper:
    if word.upper() in row: n+=1


### if we want to use 'in' to search in list with case insensitive
# >>> [x.upper() for x in ["a","b","c"]]                                    # we need to make each of the string element become upper
# ['A', 'B', 'C']

# >>> map(lambda x:x.upper(),["a","b","c"])                                 # or map function (str.upper(), list[])
# ['A', 'B', 'C']



# regex (Regular Expression)
# // regex is a way to handle the string, by using some special symbol, to let the user to find/replace some specific string

### we can use the website http://pythex.org/ to test whether the regex result is correct.

### symbols:
#   .       represents one character aside from '\n'
#   ^       represents the beginning of the insert bar
#   $       represents the end of the insert bar
#   *       represents the previous item can appear 0 time or unlimited times   (cannot appear just 1 time)
#   +       represents the previous item can appear 1 time or unlimited times   (cannot appear 0 time)
#   ?       represents the previous item can appear 0 or 1 time                 (cannot appear more than 1 time)

### expressions:
#   [abc]   represents one character that matches 'a' or 'b' or 'c'
#   [a-c]   represents one character that matches 'a' to 'c'
#   [^a-c]  represents one character that matches any character EXCEPT 'a' to 'c'

#   {m}     represents the previous item has to appear m times
#   {m,}    represents the previous item has to appear m times and at max unlimited times
#   {m,n}   represents the previous item has to appear m times and at max n times

#   \       represents the following character should be handled like a normal character, not escape character \n, \t, \d...
#   \n      represents new line character
#   \t      represents tab character
#   \r      represents carriage return (back to the beginning of the row)

#   \d      represents a decimal number character, same as [0123456789] or [0-9]
#   \D      represents a NON decimal number character, same as [^0123456789] or [^0-9]
#   \s      represents an empty character, same as [ \r\t\n\f]
#   \S      represents a NON empty character, same as  [^ \r\t\n\f]
#   \w      represents a number, letter or underscore character, same as [0-9a-zA-Z_]
#   \W      represents a NON number, letter or underscore character, same as [^0-9a-zA-Z_]

# >>> examples:
#   [0-9]+                              integer (character of 0-9 can appear multiple times)        // e.g. 33025, 2859, 337
#   [0-9]+\.[0-9]+                      real number with decimal point (0-9 decimal_point 0-9)      // e.g. 75.93, 3.14, 920.281
#   [A-Za-z]+                           English word (character of upper/lower letter multi times)  // e.g. Python, Programming, Udemy
#   [A-Za-z_][A-Za-z0-9_]*              variable name (letter or underscore, letter or num or _)    // e.g. _pointer, total, num1
#   [a-zA-Z0-9\._]+@[a-zA-Z0-9\._]+     Email (letter or num or _ or . @ letter or num or _ or . )  // e.g. guest@gmail.com, derrick.123456789@hotmail.com
#   https://[a-zA-Z0-9\./_]+            URL(https) (https:// letter or num or . or / or _)          // e.g. https://www.google.com/


# create regex objects (using re package)
# // to use regex, we need to import re package, and use the compiling methods from re package to create a regex object
import  re
word = re.compile('[a-z]+')

# // after creating the regex object, we can use the following methods to search for specific string:
#    match(string)
#    search(string)
#    findall()
