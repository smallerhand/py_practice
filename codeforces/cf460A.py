n, m = map(int, input().split(' '))

t = 1
while n > 0:
    n = n - 1
    if t%m==0:
        n += 1
    if n == 0:
        break
    t += 1

print(t)