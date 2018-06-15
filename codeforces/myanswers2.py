#Codeforces Round #487
#A
s = input()
output = 'No'
for i in range(len(s)-2):
    if s[i:i+3] in ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']:
        output = 'Yes'
        break;
    
print(output)

#lst = [int(i) for i in s]
#B (wrong in pretest 6)
n, p = map(int, input().split(' '))
s = input()
output = 'No'
x = int(n/p)
if n > p:
    for i in range(len(s)):
        if s[i] == '0':
            for j in range(x):
                if i+(j+1)*p < len(s):
                    if s[i+(j+1)*p] == '.':
                        check = i+(j+1)*p
                        output = ''
                        for k in range(len(s)):
                            if k < check:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                            elif k == check:
                                output += '1'
                            else:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'    
        elif s[i] == '1':
            for j in range(x):
                if i+(j+1)*p < len(s):
                    if s[i+(j+1)*p] == '.':
                        check = i+(j+1)*p
                        output = ''
                        for k in range(len(s)):
                            if k < check:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                            elif k == check:
                                output += '0'
                            else:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
        else:
            for j in range(x):
                if i+(j+1)*p < len(s):
                    if s[i+(j+1)*p] == '0':
                        check = i
                        output = ''
                        for k in range(len(s)):
                            if k < check:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                            elif k == check:
                                output += '1'
                            else:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                    if s[i+(j+1)*p] == '1':
                        check = i
                        output = ''
                        for k in range(len(s)):
                            if k < check:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                            elif k == check:
                                output += '0'
                            else:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'

print(output)

#C. (문제를 잘 모르겠음)
a, b, c, d = map(int, input().split(' '))

#output1 = str(x) + ' ' + str(y)
output = []
output[1] = ''

#print(output1)
for i in range(x):
    print(output[i])
    
#D. (error)
n, l, w = map(int, input().split(' '))
x = []
v = []
for i in range(n):
    xi, vi = map(int, input().split(' '))
    x.append(xi)
    v.append(vi)
output = 0

for i in range(n-1):
    for j in range(i+1, n):
        if x[i] * x[j] > 0:
            if v[i] * v[j] > 0:
                output += 1
            else:
                if abs(v[i]) < w and abs(v[j]) < w:
                    output += 1
        elif x[i] * x[j] < 0:
            if v[i] * v[j] < 0:
                output += 1
            else:
                if abs(v[i]) < w and abs(v[j]) < w:
                    output += 1
        elif x[i] == 0:
            if abs(v[i]) < w:
                if (v[j] - x[i])*x[j] < 0:
                    output += 1
        elif x[j] == 0:
            if abs(v[j]) < w:
                if (v[i] - x[j])*x[i] < 0:
                    output += 1
                    
print(output)



