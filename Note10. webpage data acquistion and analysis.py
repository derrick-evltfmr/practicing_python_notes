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

# // we can use 'in' or regular expression(regex) to query the data that matched
import requests
url = "http://books.toscrape.com/"
html = requests.get(url)
html.encoding = "utf-8"
print(html.text)                                                            # this is the source code of the webpage that read from utf-8 encoding format

htmllist = html.text.splitlines()                                            # However, the way above includes the new line characters
for row in htmllist:                                                        # by using splitlines(), we can split the source code into rows without new line characters
    print(row)