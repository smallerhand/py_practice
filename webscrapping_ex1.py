#�Ѱܷ����� ������ �̹��� �ٿ�ε�
import os
from os.path import exists
from bs4 import BeautifulSoup as bs
import urllib.request as req
#���� ������ ���丮 �ִ��� Ȯ��, ������ ����
word=input('������ ���丮 �̸��� �Է��ϼ��� :')
if not exists('desktop/python/'+word):
    os.mkdir('desktop/python/'+word)
    print('[%s]���丮�� �����߽��ϴ�.'%word)
else:
    print('[%s]���丮�� �����մϴ�.'%word)
#�ش� ���丮�� ��� ���� �ִ��� a������ ��Ƶ�.
a=len(os.listdir('desktop/python/'+word))
x=0
for i in range(10):
url="http://search.hani.co.kr/Search?command=query&keyword=%EB%AC%B8%EC%9E%AC%EC%9D%B8&media=multimedia&sort=d&period=all&datefrom=2000.01.01&dateto=2018.03.31&pageseq="+str(i)
    res=req.urlopen(url)
    soup=bs(res,"html.parser")
    lst=soup.select("#contents > div.search-result-section > ul > li > p.photo > a > img")
#���� �����ϸ鼭 �ϳ� ������ ������ x������ 1�� ������Ŵ.
    for j in lst:
        with open('desktop/python/'+word+'/'+j.attrs['src'].split('/')[-1],'wb') as w:
            imgfile=req.urlopen(j.attrs['src'].replace('/120/120/','/1000/1000/')).read()
            w.write(imgfile)
            x+=1
        if x%10==0:
            print(str(x)+'�� �����Ͽ����ϴ�')
#�� ���� �����ߴ��� ����Ʈ�ϸ鼭 �۾� ����.(�ߺ��� ������ ��������, ���������� ���� �����ߴ����� ���)
print('�� '+str(x)+'�� �����Ͽ����ϴ�.')
b=len(os.listdir('desktop/python/'+word))
print('���丮�� '+str(b-a)+'�� ���� �߰���. ('+str(x-b+a)+'�� ������ �ߺ�)')
print('���� ���� �Ϸ�')    
