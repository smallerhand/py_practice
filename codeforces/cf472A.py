#다시
n = int(input())
A = 4
B = n-A
   
whatA = False
whatB = False

while not (whatA and whatB):
    rootB = int(B**(1/2))
    whatB = False
    for i in range(rootB):
        if i < 2:
            continue
        elif B%i==0:
            whatB = True
            break
    rootA = int(A**(1/2))
    whatA = False
    for i in range(rootA):
        if i < 2:
            continue
        elif A%i==0:
            whatA = True
            break
    if not (whatA and whatB):
        A += 1
        B -= 1
        
        
print(A, B)

