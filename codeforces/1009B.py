#1009B. Minimum Ternary String
s = input()
s = list(s)
l = len(s)

#2이면, 0이나 1이면, 다시 2가 나오기 전까지 카운트하고 111112200 이렇게
#1이면, 0이면, 2가 나오기 전까지 카운트하고 0000011 이렇게

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

                        
output = ''
for i in s:
    output += i

print(output)





