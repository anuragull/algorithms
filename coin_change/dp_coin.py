import sys
import math
import decimal
import numpy
valid_denom = [1, 4, 6]

def dp_coin(n):
    minCoins = numpy.zeros(n+1)
    denom = numpy.zeros(n+1)
    for i in range(1, n+1):
        minCoins[i] = decimal.Decimal('Infinity')
	for j in valid_denom:	    
            if i >= j and (1 +  minCoins[i - j] < minCoins[i]):
	        minCoins[i] = 1 + minCoins[i - j]
                denom[i] = j
    return minCoins[n], denom


def print_coin(denom, k):
    if k > 0:
        print_coin(denom, k - denom[k])
        sys.stdout.write(str(denom[k]) + ',')
    
if __name__ == "__main__":
    change_amount = int(sys.argv[1])
    coins, denom = dp_coin(change_amount)
    print("min coins requred %d" % coins)
    print("Coins denominations used ")
    print_coin(denom, change_amount) 
    print("\n")


