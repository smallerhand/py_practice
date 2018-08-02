a, b = map(int, input().split(' '))

out = a
nam = 0
while a>0:
    a, nam = divmod(a+nam, b)
    out += a

print(out)