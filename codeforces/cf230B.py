#time limit on test33
#개선했더니, wrong on test16
#다시 개선했더니, time limit on test7
#갈수록 나빠지고 있음.

n = int(input())
xline = input().split(' ')
x = [int(i) for i in xline]

def jegobinya(t):
    root = int(t**(1/2))
    if root**2 == t:
        return root
    return 0

maxroot = int(max(x)**(1/2))+1
arr = [1 for i in range(maxroot)]

def sossu(array):
    array[0] = 0
    leng = len(array)
    for i in range(3, leng, 2):
        array[i] = 0
    for i in range(5, leng, 3):
        array[i] = 0
    for i in range(3, leng):
        if array[i] == 0:
            continue
        else:
            for j in range(2*i-1, leng, i):
                array[j] = 0
    return array

arr = sossu(arr)

def sossunya(array, t):
    if array[t-1] == 1:
        return True
    return False
    
for i in x:
    root = jegobinya(i)
    if i < 3:
        print('NO')
    elif root != 0:
        if sossunya(arr, root):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
        

#다시 처음부터
n = int(input())
xline = input().split(' ')
x = [int(i) for i in xline]

def jegobinya(t):
    root = int(t**(1/2))
    if root**2 == t:
        return root
    return 0

jegoblist = [0 for i in range(n)]
i = 0
testlist = []
for xi in x:
    k = jegobinya(xi)
    jegoblist[i] = k
    testlist.append(k)
    i += 1

maxroot = int(max(testlist)**(1/2))

def makingsossulist(maxroot):
    sossulist = [2]
    if maxroot+1 > 4:
#keep        
    
