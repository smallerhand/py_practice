line1 = input()
line2 = input()

l1 = [int(i) for i in line1]
l2 = [int(i) for i in line2]

output = ''

for i in range(len(l1)):
    if l1[i]-l2[i] != 0:
        output += str(1)
    else:
        output += str(0)
        
print(output)