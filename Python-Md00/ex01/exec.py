import sys, string

def reverse(string):
    return string.swapcase()[::-1]

if len(sys.argv) > 1:
    tmp = ' '.join(sys.argv[1:])
    result = reverse(tmp)
    print(result)
else:
    print("")
