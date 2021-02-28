from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("http://www.pythonscraping.com/pages/error.html")
    print(html.read())
    
except HTTPError as e:
   print(e)
except URLError as e:
    print(e)