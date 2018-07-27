line = input()
line = line[1:-1].split(', ')

if line == ['']:
    print(0)
else:
    print(len(set(line)))