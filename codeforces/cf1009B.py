#1009B. Minimum Ternary String (Time limit on test4)
s = input()
s = list(s)
l = len(s)

while True:
    asis = s[:]
    for i in range(l):
        if s[i] == '1':
            start = i
            zero = 0
            one = 1
            for j in range(l-i-1):
                if s[i+j+1] == '2':
                    break
                elif s[i+j+1] == '0':
                    zero += 1
                else:
                    one += 1
            if zero != 0:                
                for i in range(zero):
                    s[start+i] = '0'
            for i in range(one):
                s[start+zero+i] = '1'
    
    for i in range(l):
        if s[i] == '2':
            start = i
            zero = 0
            one = 0
            two = 1
            for j in range(l-i-1):
                if s[i+j+1] == '2':
                    break
                elif s[i+j+1] == '0':
                    zero += 1
                else:
                    one += 1
            if one != 0:
                for i in range(one):
                    s[start+i] = '1'
                for i in range(two):
                    s[start+one+i] = '2'
                if zero != 0:
                    for i in range(zero):
                        s[start+one+two+i] = '0'
    if asis == s:
        break

                        
output = ''
for i in s:
    output += i

print(output)


