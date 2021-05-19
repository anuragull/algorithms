"""

count the bits that are set to one in x


assumption: integers only 
assertive test case: 2 --> 1, 
corner test case: 2 ^ 64 
algorithm performance analysis: 
time analysis: O(n) to number of bits
space analysis: O(1)
"""
import sys

def count_bits(x):
    num_bits = 0
    while(x):
        num_bits += x & 1 
        x >>= 1
    return num_bits

def test():
    assert count_bits(2) == 1
    assert count_bits(3) == 2

if __name__ == "__main__":
    val = sys.argv[1]
    output = count_bits(int(val))
    print(output)
    test()

