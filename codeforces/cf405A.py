n = int(input())
aline = input().split(' ')
a = [int(i) for i in aline]

for j in range(n-1):
    for i in range(n-1):
        if a[i] > a[i+1]:
            k = a[i]
            a[i] = a[i+1]
            a[i+1] = k

output = ''
for i in a[:-1]:
    output += str(i)+' '
output+=str(a[-1])
print(output)