#A pass
n = int(input())
xline = input().split(' ')
yline = input().split(' ')
x = [int(i) for i in xline]
y = [int(i) for i in yline]

yes = 'YES'
no = 'NO'

if sum(x) >= sum(y):
    print(yes)
else:
    print(no)
    
#B
n, x = map(int, input().split(' '))
aline = input().split(' ')
a = [int(i) for i in aline]
b = [0 for i in a]
c = [0 for i in a]
cnt = 0

if len(set(a)) != len(a):
    print(cnt)
else:
    cnt += 1
    for i in range(n):
        b = a[:]
        c = a[:]
        b.remove(a[i])
        if int(bin(a[i]&x), 2) in b:
            print(1)
            break
        else:
            c[i] = int(bin(a[i]&x), 2)
        if i == n-1:
            if len(set(c)) < n:
                print(2)
            else:
                print(-1)    
    
#C
n = int(input())
aline = input().split(' ')
a = [int(i) for i in aline]
a.sort()
x = [0 for i in range(n)]
y = [0 for i in range(n)]

for i in range(n) :
    x[i] = a[i]
    y[i] = a[2*n-i-1]

print((max(x) - min(x))*(max(y) - min(y)))


#D
n, m, q = map(int, input().split(' '))
rc = [[0]*m for i in range(n)]
for i in range(q):
    r, c = map(int, input().split(' '))
    rc[r-1][c-1] = 1

if n == 1 or m == 1:
    print(n*m-q)
else:
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            passornot = False
            if rc[i][j] == 1:
                continue
            else:
                for k in range(n):
                    if k == i:
                        continue
                    elif rc[k][j] == 1:
                        for l in range(m):
                            if l == j:
                                continue
                            elif rc[k][l] == 1:
                                if rc[i][l] == 1:
                                    passornot = True
                                    break
                    if passornot:
                        break
                    if i == n-1:
                        if k == n-2 and l == m-1:
                            cnt += 1
                            print(i,j,k,l,cnt)
                            break
                    elif k == n-1 and l == m-1:
                        cnt+=1
                        print(i,j,k,l,cnt)
    print(cnt)

#E
n = int(input())
aline = input().split(' ')
a = [int(i) for i in aline]

rounded = n/2
if rounded - int(rounded) >= 0.5:
    rounded = int(rounded) + 1
else:
    rounded = int(rounded)

res = [0 for i in range(rounded)]

if rounded == 1:
    print(res)
else:
    output = ''
    for i in res[:-1]:
        output += str(i)+' '
    output += str(res[-1])
    print(output)



