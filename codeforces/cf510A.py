n, m = map(int, input().split(' '))
line = ['' for i in range(n)]
cnt = int(n/2) + 1

for i in range(cnt):
    line[i*2] = '#' * m
    if i*2+1 <= n-1:
        if i%2 == 0:
            for j in range(m):
                if j < m-1:
                    line[i*2+1] += '.'
                else:
                    line[i*2+1] += '#'
        else:
            for j in range(m):
                if j == 0:
                    line[i*2+1] += '#'
                else:
                    line[i*2+1] += '.'

for i in range(n):
    print(line[i])
