"""


Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


"""

# constraint : carry, over ; max over
# test : "1" + "9" , "" "", "101" + "95" [variable length, empty, carry_over]
# ideas : get the mex length, iterate over in reverese order and 
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a_len = len(num1)
        b_len = len(num2)
        max_len = a_len if a_len >= b_len else b_len 
        carry = 0
        i = 0
        st = ""
        num_lst = []
        while(i < max_len) :
            a = b = 0
            if i < a_len:
                a = int(num1[a_len - 1 -i])
            if i < b_len:
                b = int(num2[b_len - 1 - i])
            total =  a + b + carry
            if total >= 10:
                carry = 1
                total = total % 10
            else:
                carry = 0
            st = str(total) + st
            i+= 1
        if carry:
            st = str(carry) + st
        return st
