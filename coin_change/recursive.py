import sys
import math
import decimal
valid_denom = [1, 4, 6]

def change(n):
    print(n)
    if n < 0:
        return decimal.Decimal('Infinity')
    elif n==0:
        return 0
    else:
        return 1 + min([change(n -x) for x in valid_denom])

def test():
    pass
    
if __name__ == "__main__":
    print(change(int(sys.argv[1])))




