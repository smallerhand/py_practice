n = int(input())
s = input()
slist = [0 for i in range(n)]
if len(s) < 26:
    print('NO')
else:
    for i in range(n):
        ords = ord(s[i])
        if ords >= 97:
            ords -= 32
        slist[i] = ords
    if len(set(slist)) == 26:
        print('YES')
    else:
        print('NO')
