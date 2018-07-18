#Codeforces Round #487
#A
s = input()
output = 'No'
for i in range(len(s)-2):
    if s[i:i+3] in ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']:
        output = 'Yes'
        break;
    
print(output)

#lst = [int(i) for i in s]
#B (wrong in pretest 6)
n, p = map(int, input().split(' '))
s = input()
output = 'No'
x = int(n/p)
if n > p:
    for i in range(len(s)):
        if s[i] == '0':
            for j in range(x):
                if i+(j+1)*p < len(s):
                    if s[i+(j+1)*p] == '.':
                        check = i+(j+1)*p
                        output = ''
                        for k in range(len(s)):
                            if k < check:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                            elif k == check:
                                output += '1'
                            else:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'    
        elif s[i] == '1':
            for j in range(x):
                if i+(j+1)*p < len(s):
                    if s[i+(j+1)*p] == '.':
                        check = i+(j+1)*p
                        output = ''
                        for k in range(len(s)):
                            if k < check:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                            elif k == check:
                                output += '0'
                            else:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
        else:
            for j in range(x):
                if i+(j+1)*p < len(s):
                    if s[i+(j+1)*p] == '0':
                        check = i
                        output = ''
                        for k in range(len(s)):
                            if k < check:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                            elif k == check:
                                output += '1'
                            else:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                    if s[i+(j+1)*p] == '1':
                        check = i
                        output = ''
                        for k in range(len(s)):
                            if k < check:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                            elif k == check:
                                output += '0'
                            else:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'

print(output)

#C. (문제를 잘 모르겠음)
a, b, c, d = map(int, input().split(' '))

#output1 = str(x) + ' ' + str(y)
output = []
output[1] = ''

#print(output1)
for i in range(x):
    print(output[i])
    
#D. (error)
n, l, w = map(int, input().split(' '))
x = []
v = []
for i in range(n):
    xi, vi = map(int, input().split(' '))
    x.append(xi)
    v.append(vi)
output = 0

for i in range(n-1):
    for j in range(i+1, n):
        if x[i] * x[j] > 0:
            if v[i] * v[j] > 0:
                output += 1
            else:
                if abs(v[i]) < w and abs(v[j]) < w:
                    output += 1
        elif x[i] * x[j] < 0:
            if v[i] * v[j] < 0:
                output += 1
            else:
                if abs(v[i]) < w and abs(v[j]) < w:
                    output += 1
        elif x[i] == 0:
            if abs(v[i]) < w:
                if (v[j] - x[i])*x[j] < 0:
                    output += 1
        elif x[j] == 0:
            if abs(v[j]) < w:
                if (v[i] - x[j])*x[i] < 0:
                    output += 1
                    
print(output)

#510B. Fox And Two Dots (보류)
n, m = map(int, input().split(' '))
matrix = [['' for col in range(m)] for row in range(n)]
dic = dict()
for i in range(n):
    lst = input()
    for j in range(m):
        matrix[i][j] = lst[j]
        if lst[j] in dic.keys():
            dic[lst[j]].append((i,j))
        else:
            dic[lst[j]] = [(i,j)]
            
output = 'No'        

for factor in dic.keys():
    if len(dic[factor]) >= 4:
        for i in range(n):
            lst = []
            for k in dic[factor]:
                if k[0] == i:
                    lst.append(k[1])
            start = min(lst)
            end = max(lst)
            print(start, end)
        for j in range(m):
            lst = []
            for l in dic[factor]:
                if l[1] == j:
                    lst.append(l[0])
            start = min(lst)
            end = max(lst)
            print(start, end)

cnt = 1

if cnt >= 4:
    output = 'Yes'
    
print(output)

#339B. Xenia and Ringroad
n, m = map(int, input().split(' '))
alist = input().split(' ')
alist = [int(i) for i in alist]

time = 0

for i in range(m):
    if i == m-1:
        time += alist[i] - 1
    elif alist[i] > alist[i+1]:
        time += n
    else:
        continue
    
print(time)

#492B. Vanya and Lanterns
n, l = map(int, input().split(' '))
alist = input().split(' ')
a = [int(i) for i in alist]

a.sort()
if a[0] != 0:
    max = a[0]*2
else:
    max = 0

if a[-1] != l:
    if max < (l - a[-1])*2:
        max = (l - a[-1])*2

for i in range(n-1):
    if max < a[i+1] - a[i]:
        max = a[i+1] - a[i]

d = max/2
print("{0:.10f}".format(d))

#200B. Drinks
n = int(input())
line = input().split(' ')
p = [int(i) for i in line]

print(sum(p)/n)

#4C. Registration system
n = int(input())
line = ['' for i in range(n)]
dic = dict()
for i in range(n):
    inp = input()
    if inp in dic.keys():
        dic[inp] += 1
        line[i] = inp + str(dic[inp])
    else:
        dic[inp] = 0
        line[i] = inp
        
for i in range(n):
    if line[i].isalpha():
        print('OK')
    else:
        print(line[i])

#230B. T-primes (wrong on test16)
n = int(input())
xline = input().split(' ')
x = [int(i) for i in xline]

for i in range(n):
    end = False
    integer = x[i]
    if integer in [1,2,3,16,36,64]:
        print('NO')
    else:
        root = int(integer**(1/2))
        root_of_root = int(root**(1/2))
        if root ** 2 == integer:
            if root_of_root <= 2:
                print('YES')
            else:
                for j in range(2, root_of_root):
                    if root%j == 0:
                        break
                    elif j == root_of_root-1:
                        print('YES')
                        end = True
                if not end:
                    print('NO')                
        else:
            print('NO')
                    
#230B. T-primes (wrong on test16)
n = int(input())
xline = input().split(' ')
x = [int(i) for i in xline]

for i in range(n):
    obj = x[i]
    end = True
    if obj == 1:
        end = False
    else:
        root = int(obj**(1/2))
        if root**2 == obj:
            root_of_root = int(root**(1/2))
            if root_of_root**2 == root:
                for j in range(root_of_root):
                    if j in [0,1]:
                        continue
                    elif root % j == 0:
                        end = False
                        break
            else:
                for j in range(root_of_root+1):
                    if j in [0,1]:
                        continue
                    elif root % j == 0:
                        end = False
                        break
        else:
            end = False
    if end:
        print('YES')
    else:
        print('NO')
                        
#489C. Given Length and Sum of Digits... (wrong on test29)
m, s = map(int, input().split(' '))

if m == 1 and s < 10:
    print(s, s)
elif m*9 < s or (m>1 and s==0):
    print(-1, -1)
else:
    mok, nam = divmod(s, 9)
    aida = m - mok - 1
    if nam == 0 and mok == m:
        output = '9'*m
        print(int(output), (output))
    elif nam == 0:
        output = '1'+(m-mok-2)*'0'+'8'+(mok-1)*'9'
        output2 = (mok-1)*'9'+'8'+(m-mok-2)*'0'+'1'
        print(int(output), int(output2))
    else:
        output2 = mok*'9'+str(nam)+aida*'0'
        if aida > 0:
            output = '1'+(aida-1)*'0'+str(nam-1)+mok*'9'
        else:
            output = str(nam)+mok*'9'
        print(int(output), int(output2))

#519B. A and B and Compilation Errors
n = int(input())
aline = input().split(' ')
bline = input().split(' ')
cline = input().split(' ')
a = [int(i) for i in aline]
b = [int(i) for i in bline]
c = [int(i) for i in cline]

def dicfunc(abc):
    dic = dict()
    for i in abc:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

dica, dicb, dicc = dicfunc(a), dicfunc(b), dicfunc(c)

for i in dica.keys():
    if (i not in dicb.keys()) or (dica[i] > dicb[i]):
        print(i)
        break

for i in dicb.keys():
    if (i not in dicc.keys()) or (dicb[i] > dicc[i]):
        print(i)
        break

#268B. Buttons
n = int(input())

def push(n):
    output = 0
    for i in range(n-1):
        output += (n-i-1)*(i+1)
    output += n
    return output

print(push(n))

#489B. BerSU Ball
n = int(input())
aline = input().split(' ')
m = int(input())
bline = input().split(' ')
a = [int(i) for i in aline]
b = [int(i) for i in bline]

sorted_a = sorted(a)
sorted_b = sorted(b)

def count_match(sorteda, i, sortedb, count):
    if (i == len(sorteda)) or (len(sortedb) == 0):
        return count
    elif sorteda[i]-1 in sortedb:
        sortedb.remove(sorteda[i]-1)
        return count_match(sorteda, i+1, sortedb, count+1)
    elif sorteda[i] in sortedb:
        sortedb.remove(sorteda[i])
        return count_match(sorteda, i+1, sortedb, count+1)
    elif sorteda[i]+1 in sortedb:
        sortedb.remove(sorteda[i]+1)
        return count_match(sorteda, i+1, sortedb, count+1)
    else:
        return count_match(sorteda, i+1, sortedb, count)

count = count_match(sorted_a, 0, sorted_b, 0)

print(count)

#474B. Worms(time limit on test12)
n = int(input())
aline = input().split(' ')
m = int(input())
qline = input().split(' ')
a = [int(i) for i in aline]
q = [int(i) for i in qline]
sumofa = 0
acum = [0 for i in range(n)]
for i in range(n):
    sumofa += a[i]
    acum[i] = sumofa
for i in q:
    M = int(n/2)
    L = 0
    H = n-1
    while True:
        if i == acum[M]:
            print(M+1)
            break
        elif i < acum[M]:
            if (M == 0) or (i > acum[M-1]):
                print(M+1)
                break
            else:
                H = M-1
                M = int((L+H)/2)
        else:
            L = M+1
            M = int((L+H)/2)

#588A. Duff and Meat
n = int(input())
a = [0 for i in range(n)]
p = [0 for i in range(n)]
for i in range(n):
    a[i], p[i] = map(int, input().split(' '))

money = 0
minp = p[0]
for i in range(n):
    if minp <= p[i]:
        money += a[i]*minp
    else:
        minp = p[i]
        money += a[i]*minp
        
print(money)

#467B. Fedor and New Game(아직 문제파악중)
n, m, k = map(int, input().split(' '))
타입, 병사수, 타입
x = [0 for i in range(m+1)]
for i in range(m+1):
    x[i] = int(input())

def tobinary(integ):
    res = ''
    while True:
        mok, nam = divmod(integ, 2)
        res = str(nam) + res
        integ = mok
        if mok == 0:
            break
    return res

print(tobinary(8), tobinary(5), tobinary(111), tobinary(17))

print(tobinary(1), tobinary(2), tobinary(3), tobinary(4))

#520B. Two Buttons
n,m=map(int,input().split(' '))
cnt=0
while n!=m:
    cnt+=1
    if n<m:
        if m%2==0:
            m/=2
        else:
            m+=1
    else:
        m+=1
print(cnt)

#136A. Presents
n = int(input())
pline = input().split(' ')
p = [int(i) for i in pline]
q = [0 for i in range(n)]
for i in range(n):
    q[p[i]-1] = i+1
res = ''
for i in range(n-1):
    res += str(q[i])+' '
res += str(q[-1])
print(res)

#230B. T-primes (time limit test 33)
n = int(input())
xline = input().split(' ')
x = [int(i) for i in xline]

class matsuja:
    def __init__(self, inte):
        self.integer = inte
        self.root = int(inte**(1/2))
    def jegobinya(self):
        if self.root**2 == self.integer:
            return True
        else:
            return False
    def sossunya(self):
        rofr = int(self.root**(1/2))
        for i in range(rofr+1):
            if i in [0,1]:
                continue
            elif self.root % i == 0:
                return False
        return True

for i in x:
    if i!=1 :
        A = matsuja(i)
        if A.jegobinya():
            if A.sossunya():
                print('YES')
                continue
    print('NO')

#486A. Calculating Function
n = int(input())
if n%2==0:
    print(int(n/2))
else:
    print(int((n-1)/2)-n)

#617A. Elephant
x = int(input())
if x <= 5:
    print(1)
elif x % 5 == 0:
    print(int(x/5))
else:
    print(int(x/5)+1)
 
#208A. Dubstep
word = input().split('WUB')
reword = ''
for i in word:
    if i =='':
        continue
    else:
        reword += i + ' '
print(reword[:-1])

#318A. Even Odds
n, k = map(int, input().split(' '))
if n%2==0:
    if k*2>n:
        print(k*2-n)
    else:
        print(k*2-1)
else:
    if k*2-1>n:
        print(k*2-n-1)
    else:
        print(k*2-1)    
        
#1009A. Game Shopping
