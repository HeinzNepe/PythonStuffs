import sys

Number1 = input("Number \n")
try:
    Number1 = int(Number1)
except:
    print("This is not a number")
    sys.exit("NAN")

Number2 = input("Number \n")

try:
    Number2 = int(Number2)
except:
    print("This is not a number")
    sys.exit("NAN")

Result = Number1 * Number2

print(Result)
