n = int(input())
h = [0 for i in range(n)]
a = [0 for i in range(n)]

for i in range(n):
    H, A = map(int, input().split(' '))
    h[i] = H
    a[i] = A

cnt = 0

for i in h:
    for j in a:
        if i==j:
            cnt+=1

print(cnt)