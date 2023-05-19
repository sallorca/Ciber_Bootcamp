import sys

def check_number(num):
    if num == 0:
        return "I'm Zero."
    elif num % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."

if len(sys.argv) == 2 and sys.argv[1].isdigit():
    num = int(sys.argv[1])
    result = check_number(num)
    print(result)
else:
    if len(sys.argv) == 1:
        print(" ")
    elif not sys.argv[1].isdigit():
        print("AssertionError: argument is not an integer")
    else:
        print("AssertionError: more than one argument are provided")
