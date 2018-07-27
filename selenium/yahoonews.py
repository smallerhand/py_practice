from selenium import webdriver
url = "https://news.yahoo.co.jp/"
driver = webdriver.PhantomJS("desktop/python/phantomjs-2.1.1-macosx/bin/phantomjs")
driver.implicitly_wait(3)
driver.get(url)
driver.execute_script("var body = document.getElementsByTagName('body')[0]; body.setAttribute('background-color', 'white')")
driver.execute_script('document.body.style.background = "white"')
driver.save_screenshot("/Users/kimseunghyuck/Desktop/git/py_practice/selenium/frontpage.png")
driver.quit()

from bs4 import BeautifulSoup as bs
import urllib.request as req
url = "https://news.yahoo.co.jp/"
res=req.urlopen(url)
soup=bs(res, "html.parser")
cnt=0
for i in soup.findAll(class_='ttl'):
    print(i.string)
    cnt+=1
    print(cnt)
    
for link in soup.findAll('a'):
    print(link.get('href'))
    cnt+=1
    print(cnt)
cnt=0
linklist=[]
for item in soup.find_all(attrs={'class': 'ttl'}):
    for link in item.find_all('a'):
        linklist.append(link.get('href'))
        cnt+=1
print(cnt)

url = linklist[0]
res = req.urlopen(url)
soup = bs(res,"html.parser")
result = soup.find_all('p', class_='hbody')
for i in result:
    print(i.get_text(strip=True))



