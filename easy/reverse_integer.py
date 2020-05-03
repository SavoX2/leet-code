# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321

# Example 2:

# Input: -123
# Output: -321

# Example 3:

# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # cheating
        # string = str(x)
        # res = 0
        # if x >= 0:
        #     res = int(string[::-1])
        # else: 
        #     string = string[1::]
        #     res = -int(string[::-1])
        
        # if res not in range(-2**31, 2**31 - 1): 
        #     return 0
        
        # return res

        res = 0
        # % is modulo operator, and not remainder, this is why we set x=|x|
        # problem example: 5 % 3 = 2, but -5 % 3 = 1
        neg = x < 0
        x = abs(x)
        while x != 0:
            res = res * 10 + x % 10
            x //= 10
        
        if res not in range(-2**31, 2**31 - 1): 
            return 0
        
        return res if not neg else -res

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(123))
    print(sol.reverse(-123))
    print(sol.reverse(120))
    print(sol.reverse(1534236469))

# Cheating: 
# Runtime: 32 ms, faster than 57.14% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.6 MB, less than 5.26% of Python3 online submissions for Reverse Integer.

# Runtime: 24 ms, faster than 95.15% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Reverse Integer.