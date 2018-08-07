n = int(input())
nameline = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']

if n <= 5:
    print(nameline[n-1])
else:
    five = 5
    minus = 2
    while True:
        nkeep = n - five
        if nkeep > 0:
            n = nkeep
            minus *= 2
            five *= 2
        else:
            break    
    n = int((n-1)*2/minus)
    print(nameline[n])
    
