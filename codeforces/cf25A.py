n = int(input())
line = input().split(' ')
l = [int(i) for i in line]

evenness0 = False
evenness1 = False
if l[0]%2 == 0:
    evenness0 = True
if l[1]%2 == 0:
    evenness1 = True

ind = 3
if evenness0 and evenness1:
    for i in l[2:]:
        if i%2!=0:
            print(ind)
            break
        ind+=1
elif evenness0:
    if l[2]%2==0:
        print(2)
    else:
        print(1)
elif evenness1:
    if l[2]%2==0:
        print(1)
    else:
        print(2)
else:
    for i in l[2:]:
        if i%2==0:
            print(ind)
            break
        ind+=1
        