#다시
n = int(input())

if n%2==0:
    A = int(n/2)
    B = int(n/2)
else:
    A = int((n-1)/2)
    B = int((n+1)/2)


br = False
br2 = False

while True:
    rootA = int(A**(1/2))
    rootB = int(B**(1/2))
    
    for i in range(rootA):
        if i < 2:
            continue
        elif A%i==0:
            A -= 1
            B += 1
            continue
        if i == rootA-1:
            br = True
    for i in range(rootB):
        if i < 2:
            continue
        elif B%i==0:
            A -= 1
            B += 1
            continue
        if i == rootB-1:
            br2 = True
    if br and br2:
        break
        
print(A, B)