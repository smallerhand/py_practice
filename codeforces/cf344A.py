n = int(input())
char = [0 for i in range(n)]
for i in range(n):
    char[i] = int(input())

output = 1
for i in range(n-1):
    if char[i] == char[i+1]:
        continue
    else:
        output+=1
print(output)