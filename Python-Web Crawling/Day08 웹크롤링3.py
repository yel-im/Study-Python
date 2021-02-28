from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')



p = re.compile('[..]/img/gifts/img.[.]jpg')
m = bs.find_all('img',{'src':p})

print(m)



#for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    #print(sibling)