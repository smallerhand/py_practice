#time limit on test33
#개선했더니, wrong on test16

n = int(input())
xline = input().split(' ')
x = [int(i) for i in xline]

def jegobinya(t):
    root = int(t**(1/2))
    if root**2 == t:
        return root
    return 0

arr = [1 for i in range(int(max(x)**(1/2))+1)]

def sossunya(array, t):
    if t<=9:
        for i in range(2, t):
            if t%i==0:
                return array, str(False)
    else:
        roott = int(t**(1/2))+1
        for i in range(2, roott):
            if array[i]==0:
                continue
            elif t%i==0:
                return array, str(False)
            for j in range(i, t, i):
                array[j]=0
    return array, str(True)

res = str(False)

for i in x:
    root = jegobinya(i)
    if i < 3:
        print('NO')
    elif root != 0:
        arr, res = sossunya(arr, root)
        if res == str(True):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
        

