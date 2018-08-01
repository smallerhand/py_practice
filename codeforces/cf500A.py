n, t = map(int, input().split(' '))
aline = input().split(' ')
a = [int(i) for i in aline]

space = 1
transport = [space]
j = 0
yes = False
while space <= t:
    space += a[j]
    if t == space:
        print('YES')
        yes = True
        break
    transport.append(space)
    j = space - 1
if not yes:
    print('NO')
    
