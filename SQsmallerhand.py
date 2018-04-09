#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 10:26:04 2018

@author: kimseunghyuck
"""
            
"""    
filedir="desktop/test/"
sub="PYTHON"
name="김승혁"
import re
with open(filedir+sub+"_"+name+".txt", "r") as f:
    lst=[]
    lines=f.readlines()
    for i in lines:
        k=i.find('문제')
        if k != -1:
            res=i[k:k+6].replace('_', '')
            res=res.replace(' ', '')
            res=res.replace(']', '')
            res=re.findall('\d+', res)
            if len(res)>0:
                lst.append(int(res[0]))
lst.sort()
a, b=lst[0],lst[-1]
print("{}번 부터 {}번 문제까지 있습니다.".format(a, b))
print("다음은 없는 문제 리스트입니다.")
for i in range(a,b+1):
    if i not in lst:
        print(str(i)+'번')
"""


class SQ_smallerhand:
    dir = None
    name = None
    def __init__(self, filedir, name):
        self.dir=filedir
        self.name=name
        self.lst=[]
    def search(self, sub, encoding):
        self.sub=sub
        self.encoding=encoding
        import re
        with open(self.dir+self.sub+self.name+".txt", "r", encoding=self.encoding) as f:
            lines=f.readlines()
            for i in lines:
                k=i.find('문제')
                if k != -1:
                    res=i[k:k+6].replace('_', '')
                    res=res.replace(' ', '')
                    res=res.replace(']', '')
                    res=re.findall('\d+', res)
                    if len(res)>0:
                        self.lst.append(int(res[0]))
    def report(self, maxnum):
        self.lst.sort()
        self.maxnum=maxnum
        a, b=1,min(self.lst[-1], self.maxnum)
        print("{}번 부터 {}번 문제 중에서 없는 문제 리스트입니다.".format(a, b))
        for i in range(a,b+1):
            if i not in self.lst:
                print(str(i)+'번')
        print("없는 문제 출력 완료")

if __name__ == "__main__":
    MINE=SQ_smallerhand("desktop/test/", "김승혁")
    MINE.search("PYTHON_", "UTF-8")
    MINE.report(197)
    
    MINE5=SQ_smallerhand("desktop/test/", "김승혁")
    MINE5.search("R_", "UTF-8")
    MINE5.report(245)
    
    MINE3=SQ_smallerhand("desktop/test/", "김승혁")
    MINE3.search("SQL_", "euc-kr")
    MINE3.report(102)
    
    MINE4=SQ_smallerhand("desktop/test/", "김승혁")
    MINE4.search("PLSQL_", "euc-kr")
    MINE4.report(57)
