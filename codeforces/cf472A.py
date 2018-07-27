n = int(input())
A = 4
B = n-A
   
whatA = False
whatB = False

while not (whatA and whatB):
    whatB = False
    for i in range(B):
        if i < 2:
            continue
        elif B%i==0:
            whatB = True
            break
    whatA = False
    for i in range(A):
        if i < 2:
            continue
        elif A%i==0:
            whatA = True
            break
    if not (whatA and whatB):
        A += 1
        B -= 1
        
        
print(A, B)

