import sys

def main(argv):
    if argv.ishalfwidth():
        output = "invalid"
    else:
        if argv.isdigit():
            n = int(argv)
            if n >= 0 and n <= 1000:
                if n%3 == 0:
                    output = "idiot"
                    if '3' in str(n):
                        output = "dumb"
                elif '3' in str(n):
                    output = "stupid"
                else:
                    output = "smart"
        else:
            output = "invalid"
    print(output)

if __name__ == '__main__':
    for i in sys.argv[1:]:
        main(i)
        