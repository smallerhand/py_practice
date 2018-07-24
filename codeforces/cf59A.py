s = input()

output1 = ''
output2 = ''
small = 0
capital = 0
for i in s:
    if ord(i)>=65 and ord(i)<=90:
        output1 += chr(ord(i)+32)
        output2 += i
        capital += 1
    else:
        output1 += i
        output2 += chr(ord(i)-32)        
        small += 1

if small >= capital:
    print(output1)
else:
    print(output2)
