#wrong on test3

s, n = map(int, input().split(' '))
x = [0 for i in range(n)]
y = [0 for i in range(n)]
for i in range(n):
    x[i], y[i] = map(int, input().split(' '))

yes = True
for i in range(n):
    if x[i] > s:
        print('NO')
        yes = False
        break
    else:
        s = s - x[i] + y[i]
if yes:
    print('YES')

