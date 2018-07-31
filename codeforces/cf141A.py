As = input()
Bs = input()
Cs = input()

A = [i for i in As]
B = [i for i in Bs]
C = [i for i in Cs]

already = False
already2 = False

if len(A) + len(B) == len(C):
    for a in A:
        if a in C:
            C.remove(a)
        else:
            print('NO')
            already = True
            break
    if not already:
        for b in B:
            if b in C:
                C.remove(b)
            else:
                print('NO')
                already2 = True
                break
    if not (already or already2):
        if len(C) == 0:
            print('YES')
        else:
            print('NO')
else:
    print('NO')

