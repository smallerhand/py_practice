n = int(input())
pline = input().split(' ')
aline = input().split(' ')
p = [int(i) for i in pline]
a = [int(i) for i in aline]

if len(set(p[1:]+a[1:]))==n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')


