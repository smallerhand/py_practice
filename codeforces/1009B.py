#1009B. Minimum Ternary String
s = input()
s = list(s)
l = len(s)

while True:
    asis = s[:]
    for i in range(l-2,-1,-1):
        if s[i:i+2] == ['1','0']:
            s[i:i+2] = ['0','1']
        elif s[i:i+2] == ['2','1']:
            s[i:i+2] = ['1','2']
        if i != l-2:
            if s[i:i+3] == ['2','0','1']:
                s[i:i+3] = ['1','2','0']
    if asis == s:
        break

output = ''
for i in s:
    output += i

print(output)

1이면, 2면, 놔둠
0이면, 1이면, 놔둠
0이면, 2이면, 놔둠
2이면, 0이면, 1이 안나오면, 놔둠
2이면, 1이면, 0이 나오기 전까지 카운트하고 111122 이렇게
2이면, 0이면, 1이면, 다시 0이나 2가 나오기 전까지 카운트하고 111112200 이렇게
1이면, 0이면, 2가 나오기 전까지 카운트하고 0000011 이렇게

def change(sent):
    i, zero, one, two = 0, 0, 0, 0
    while sent[i] != '0':
        if sent[i] == '2':
            two += 1
        elif sent[i] == '1':
            one += 1
        i += 1
        if i == len(sent):
            break
    
change('100210')
    
        



