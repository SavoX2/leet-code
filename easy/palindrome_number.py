# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:

# Coud you solve it without converting the integer to a string?

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # string version
        # return str(x) == str(x)[::-1]

        # because of the minus, every reversal would have the minuses at different locations => not palindrome
        if x < 0: 
            return False
        original_x = x
        inverted_x = 0
        while x > 0:
            inverted_x = inverted_x * 10 + x % 10
            x //= 10
        return original_x == inverted_x

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))
    print(sol.isPalindrome(-121))
    print(sol.isPalindrome(10))

# string version 
# Runtime: 44 ms, faster than 87.16% of Python online submissions for Palindrome Number.
# Memory Usage: 12.7 MB, less than 6.03% of Python online submissions for Palindrome Number.

# Runtime: 52 ms, faster than 65.53% of Python online submissions for Palindrome Number.
# Memory Usage: 12.8 MB, less than 6.03% of Python online submissions for Palindrome Number.