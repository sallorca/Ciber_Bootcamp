import sys

def operacion(a, b):

    suma = (a + b)
    resta = (a - b)
    multiplicacion = (a * b)

    print("Sum:", suma)
    print("Difference:", resta)
    print("Product:", multiplicacion)
    if(b == 0):
        print("Quotient: ERROR (division by zero)")
        print("Remainder: ERROR (modulo by zero)")
        print("")
    else:
        division = ( a / b)
        modulo = ( a % b)
        print("Quotient:", division)
        print("Remainder:", modulo)
        print("")

if __name__=="__main__":
    try:
        if len(sys.argv) == 3:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            operacion(x, y)
    except:
        print("AssertionError: only integers\n")
    if len(sys.argv) <= 1:
        print("ERROR")
    elif len(sys.argv) != 3:
        print("AssertionError: Wrong number of arguments\n")

