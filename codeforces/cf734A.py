n=int(input())
s=input()

A=0
D=0

for i in s:
    if i=='A':
        A+=1
    else:
        D+=1
if A==D:
    print('Friendship')
elif A>D:
    print('Anton')
else:
    print('Danik')