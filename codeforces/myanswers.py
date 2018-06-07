#www.codeforces.com
#4A. Watermelon 
#4이상의 짝수면 yes

A = int(input())
if (A >= 4) and (A%2==0):
    print('yes')
else :
    print('no')
    
#A. Adaptation Stories
A=int(input())
lst=input().split(' ')
s=0
r=0
for i in lst:
    s+=int(i)
    if s<0:
        r-=s
        s=0
print(r)

#1A. Theatre Square
lst=input().split(' ')

x = int(lst[0])/int(lst[2])
if x%1!=0:
    x = int(x+1)

y = int(lst[1])/int(lst[2])
if y%1!=0:
    y = int(y+1)
    
print(int(x*y))

#71A. Way Too Long Words
n=int(input())
lst=dict()

for i in range(n):
    lst[i]=input()

for i in range(n):
    if len(lst[i])>10:
        print(lst[i][0]+str(len(lst[i])-2)+lst[i][-1])
    else:
        print(lst[i])

#158A. Next Round
n, k=map(int, input().split(' '))
if n < k:
    z = n
    n = k
    k = z

lst = input().split(' ')
a = int(lst[k-1])
output = 0
for i in lst:
    if int(i)>0:
        if int(i)>=a:
            output+=1
print(output)            
        
#118A. String Task
A = input()
A = A.lower()
str = ''
for i in A:
    if i not in  ['a','o','y','e','u','i']:
        str += '.'
        str += i

print(str)

#50A. Domino piling
m, n=map(int, input().split(' '))
print(int(m*n/2))

#231A. Team
n=int(input())
output=0
for i in range(n):
    a, b, c = map(int, input().split(' '))
    if a+b+c>=2:
        output+=1
print(output)

#282A. Bit++
n=int(input())
output=0
for i in range(n):
    op = input()
    if '--' in op:
        output -=1
    else:
        output +=1
print(output)

#96A. Football
inp=input()
for i in range(len(inp)):
    if inp[i:i+7]=='0000000':
        print('YES')
        break;
    elif inp[i:i+7]=='1111111':
        print('YES')
        break;
    elif i == len(inp)-1:
        print('NO')
        
#112A. Petya and Strings
l1=input().lower()
l2=input().lower()

alp='abcdefghijklmnopqrstuvwxyz'

for i in range(len(l1)):
    if alp.index(l1[i])>alp.index(l2[i]):
        print(1)
        break;
    elif alp.index(l1[i])<alp.index(l2[i]):
        print(-1)
        break;
    elif i == len(l1)-1:
        print(0)

#339A. Helpful Maths
lst=input()
if len(lst)==1:
    output = lst
else:
    lst=lst.split('+')
    while 0==0:
        for i in range(len(lst)-1):
            if int(lst[i]) > int(lst[i+1]):
                cons = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = cons
        count = 0
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                break;
            elif i==len(lst)-2:
                count = 1
        if count == 1:
            break;
    output=lst[0]
    for i in lst[1:]:
        output += '+' + i
print(output)

#266A. Stones on the Table 
n=int(input())
s=input()
output = 0

for i in range(n-1):
    if s[i]==s[i+1]:
        output += 1
print(output)

#281A. Word Capitalization
alp='abcdefghijklmnopqrstuvwxyz'
ALP='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = input()
output = ALP[(alp+ALP).index(s[0])%26]
for i in s[1:]:
    output += i
print(output)

#158B. Taxi
n = int(input())
s = input().split(' ')
lst = [int(i) for i in s]

n1 = lst.count(1)
n2 = lst.count(2)
n3 = lst.count(3)
n4 = lst.count(4)
output4 = n4
n4 = 0
output2, n2 = divmod(n2, 2)
if n2 == 1:
    n1 -= 2
    output2 += 1
min13=min(n1, n3)
output13 = min13
n1 -= min13
n3 -= min13
if n1 == 0:
    output13 += n3
else:
    div, mod = divmod(n1, 4)
    if mod == 0:
        output13 += div
    else:
        output13 += div + 1
output = sum([output4, output2, output13])
print(output)
    
#116A. Team
n = int(input())
total = [0]
for i in range(n):
    a, b = map(int, input().split(' '))
    total.append(total[-1]-a)
    total.append(total[-1]+b)
print(max(total))

#263A. Beautiful Matrix
a, b = 0, 0
for i in range(5):
    c1, c2, c3, c4, c5 = map(int, input().split(' '))
    lst = [c1, c2, c3, c4, c5]
    if sum(lst)==1:
        a = i+1; b = lst.index(1)+1
print(abs(a-3)+abs(b-3))

#58A. Chat room
s = input()
n = len(s)
result = False
for i in range(n):
    if s[i] =='h':
        for j in range(n-i-1):
            if s[i+j+1] =='e':
                for k in range(n-i-j-2):
                    if s[i+j+k+2] =='l':
                        for l in range(n-i-j-k-3):
                            if s[i+j+k+l+3] == 'l':
                                for m in range(n-i-j-k-l-4):
                                    if s[i+j+k+l+m+4] =='o':
                                        result = True
                                        print('YES')
                                        break;
                                if result == True:
                                    break;
                        if result == True:
                            break;
                if result == True:
                    break;
        if result == True:
            break;
    elif i == n-1:
        print('NO')

#122A. Lucky Division
n=int(input())
lst=[4,7,44,77,47,444,477,747,774,447,744,474,777]
for i in lst:
    if n%i==0:
        print('YES')
        break;
    elif i == 777:
        print('NO')

#100. A+B (ACMSGURU)
A, B = map(int, input().split(' '))
output = A+B
print(output)

#131A. cAPS lOCK (wrong)
s = input()
alp='abcdefghijklmnopqrstuvwxyz'
ALP='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if len(s) == 1:
    if s in alp:
        print(ALP[alp.index(s)])
    else:
        print(s)
elif s[0] in alp:
    for i in range(len(s)-1):
        if s[i+1] in ALP:
            if i == len(s)-2:
                result = ALP[alp.index(s[0])]
                for j in s[1:]:
                    result += alp[ALP.index(j)]
                print(result)
                break;
        else:
            print(s)
            break;
else:
    for i in range(len(s)-1):
        if s[i+1] in ALP:
            if i  == len(s)-2:
                result = ''
                for j in s:
                    result += alp[ALP.index(j)]
                print(result)
                break;
        else:
            print(s)
            break;

#131A. cAPS lOCK 위 답안 왜 틀렸는지 모르겠어서 다른 방법으로 
s = input()
l = len(s)
if l == 0:
    print(s)
elif l == 1 and s.islower():
    print(s.upper())
elif s.isupper():
    print(s.lower())
elif s[0].islower() and s[1:].isupper():
    print(s[0].upper()+s[1:].lower())
else:
    print(s)
    
        
#133A. HQ9+
p = input()
if 'H' in p or 'Q' in p or '9' in p:
    print('YES')
else:
    print('NO')


#A. Diverse Team
n, k = map(int, input().split(' '))
if n < k:
    z = n
    n = k
    k = z

s = input().split(' ')
lst = [int(i) for i in s]
lst2 = list(set(lst))

if len(lst2) < k:
    print('NO')
else:
    print('YES')
    res = ''
    for j in range(k):
        res += str(lst.index(lst2[-j-1])+1)+' '
    print(res)
    
#B. Substrings Sort(Wrong in 11)
n = int(input())
lst=[]
for i in range(n):
    lst.append(input())
if n==1:
    print(lst[0])
else:    
    lst = sorted(lst, key=len)
    for j in range(n-1):
        if lst[j] in lst[j+1]:
            if j == n-2:
                print('YES')
                for k in lst:
                    print(k)
                break;
        else:
            print('NO')
            break;

#E. Divisibility by 25(error)
n = input()
if len(n) < 2 :
    print(-1)
elif len(n) == 2:
    if n in ['25', '50', '75']:
        print(0)
    elif n in ['52', '57']:
        print(1)
    else:
        print(-1)
else:
    if n[-2:] in ['25', '50', '75', '00']:
        print(0)
    else:
        lst = [int(i) for i in n]
        n0 = lst.count(0)
        n2 = lst.count(2)
        n5 = lst.count(5)
        n7 = lst.count(7)
        if n0>=2 or (n0>=1 and n5>=1) or (n2>=1 and n5>=1) or (n5>=1 and n7>=1):
            lst0, lst2, lst5, lst7 = [], [], [], []
            for i in range(n0):
                lst0.append(lst.index(0))
            for i in range(n2):
                lst2.append(lst.index(2))
            for i in range(n5):
                lst5.append(lst.index(5))
            for i in range(n7):
                lst7.append(lst.index(7))
            res = []
            if len(lst0)>1:
                m1 = 2*len(n)-lst0[-1]-lst0[-2]-3
                res.append(m1)
            if len(lst0)>0 and len(lst5)>0:
                m2 = 2*len(n)-lst0[-1]-lst5[-1]-3
                res.append(m2)
            if len(lst2)>0 and len(lst5)>0:
                m3 = 2*len(n)-lst2[-1]-lst5[-1]-3
                res.append(m3)
            if len(lst5)>0 and len(lst7)>0:
                m4 = 2*len(n)-lst5[-1]-lst7[-1]-3
                res.append(m4)
            print(min(res))
        else:
            print(-1)

#160A. Twins
n = int(input())
a = input().split(' ')
lst = [int(i) for i in a]

sorted_lst=sorted(lst)

mine = 0
yours = sum(sorted_lst)

for i in range(n):
    mine += sorted_lst[-1]
    yours -= sorted_lst[-1]
    del sorted_lst[-1]
    if mine > yours:
        print(i+1)
        break;
    
#236A. Boy or Girl
s = input()
distinct_s = set(s)
if len(distinct_s) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

#546A. Soldier and Bananas
k, n, w = map(int, input().split(' '))
output = -n
sums = (1+w)*w/2
output += sums * k
output = max(output, 0)
print(int(output))

#69A. Young Physicist
n = int(input())
X, Y, Z = 0, 0, 0
for i in range(n):
    x, y, z = map(int, input().split(' '))
    X += x; Y += y; Z += z;
if [X, Y, Z] == [0,0,0]:
    print('YES')
else:
    print('NO')
    
#467A. George and Accommodation
n = int(input())
output = 0
for i in range(n):
    p, q=map(int, input().split(' '))
    if q - p >= 2:
        output += 1
print(output)
    
#110A. Nearly Lucky Number
n = input()
count = 0
for i in n:
    if i in ['4','7']:
        count += 1
if count in [4, 7]:
    print('YES')
else:
    print('NO')

#266B. Queue at the School
n, t = map(int, input().split(' '))
s = input()
if n == 1:
    print(s)
else:
    for j in range(t):
        lst = s.split('BG')
        output = ''
        for i in lst:
            output += i + 'GB'
        s = output[:n]
    print(s)

#41A. Translation
s = input()
t = input()
s2 = ''
for i in range(len(s)):
    s2 += s[-1-i]
if s2 == t:
    print('YES')
else:
    print('NO')

#271A. Beautiful Year
y = int(input())
y2 = y + 1
while len(set([i for i in str(y2)])) < 4:
    y2 += 1
print(y2)

#337A. Puzzles
n, m = map(int, input().split(' '))
f = input().split(' ')
lst = [int(i) for i in f]
sorted_lst = sorted(lst)
mins = sorted_lst[n-1] - sorted_lst[0]
for i in range(1, m-n+1):
    data = sorted_lst[i+n-1] - sorted_lst[i]
    if data < mins:
        mins = data
print(mins)

#580A. Kefa and First Steps
n = int(input())
a = input().split(' ')
lst = [int(i) for i in a]
l = 1
maxs = 1
for i in range(n-1):
    if lst[i] <= lst[i+1]:
        l += 1
        if i == n-2:
            if maxs < l:
                maxs = l
    else:
        if maxs < l:
            maxs = l
        l = 1

print(maxs)

#842B. Gleb And Pizza http://codeforces.com/problemset/problem/842/B


