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