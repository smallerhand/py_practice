#한겨레에서 문재인 이미지 다운로드
import os
from os.path import exists
from bs4 import BeautifulSoup as bs
import urllib.request as req
#사진 저장할 디렉토리 있는지 확인, 없으면 생성
word=input('저장할 디렉토리 이름을 입력하세요 :')
if not exists('desktop/python/'+word):
    os.mkdir('desktop/python/'+word)
    print('[%s]디렉토리를 생성했습니다.'%word)
else:
    print('[%s]디렉토리에 저장합니다.'%word)
#해당 디렉토리에 몇개의 파일 있는지 a변수에 담아둠.
a=len(os.listdir('desktop/python/'+word))
x=0
for i in range(10):
    url="http://search.hani.co.kr/Search?command=query&keyword=%EB%AC%B8%EC%9E%AC%EC%9D%B8&media=multimedia&sort=d&period=all&datefrom=2000.01.01&dateto=2018.03.31&pageseq="+str(i)
    res=req.urlopen(url)
    soup=bs(res,"html.parser")
    lst=soup.select("#contents > div.search-result-section > ul > li > p.photo > a > img")
#사진 저장하면서 하나 저장할 때마다 x변수에 1씩 증가시킴.
    for j in lst:
        with open('desktop/python/'+word+'/'+j.attrs['src'].split('/')[-1],'wb') as w:
            imgfile=req.urlopen(j.attrs['src'].replace('/120/120/','/1000/1000/')).read()
            w.write(imgfile)
            x+=1
        if x%10==0:
            print(str(x)+'개 저장하였습니다')
#총 몇장 저장했는지 프린트하면서 작업 종료.(중복된 사진이 몇장인지, 최종적으로 몇장 저장했는지도 출력)
print('총 '+str(x)+'개 저장하였습니다.')
b=len(os.listdir('desktop/python/'+word))
print('디렉토리에 '+str(b-a)+'개 사진 추가됨. ('+str(x-b+a)+'개 사진은 중복)')
print('사진 저장 완료')    
