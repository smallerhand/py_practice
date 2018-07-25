n = int(input())
aline = input().split(' ')
a = [int(i) for i in aline]

argmax = 0
argmin = 0
for i in range(n):
    if a[argmax] < a[i]:
        argmax = i
    if a[argmin] >= a[i]:
        argmin = i

if argmax < argmin:
    print(argmax + n - argmin - 1)
else:
    print(argmax + n - argmin - 2)