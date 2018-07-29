n, h = map(int, input().split(' '))
aline = input().split(' ')
a = [int(i) for i in aline]
output = 0
for i in a:
    if i<=h:
        output += 1
    else:
        output += 2
print(output)