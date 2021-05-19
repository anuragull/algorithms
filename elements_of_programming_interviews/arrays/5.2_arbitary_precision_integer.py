"""
implement arbitary precision integer 

assumption : works in any fixed precision language

input : 129 --> 130, 999 --> 1000

time complexity : O(n)
space complexity : O(1)

approach : 

1. iterate the array in reverse to start with LSB
2. do grade level math, that is move the carry for next step

"""

def plus_one(A):
    carry = 0
    for i in reversed(range(len(A))):
       if i == len(A) - 1:
           new_val = A[i] + 1
       else:
           new_val = A[i] + carry
       if new_val == 10:
          A[i] = 0
          carry = 1
       else:
          A[i] = new_val
          carry = 0
    if carry == 1:
        A.insert(0, carry)
    return A

def test_plus_one():
     val = plus_one([1, 2, 9])
     print(val) 
     assert val == [1, 3, 0]
     val = plus_one([9, 9, 9])
     print(val)
     assert val == [1, 0, 0, 0]

if __name__ == "__main__":
    test_plus_one()

