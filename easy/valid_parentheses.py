# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true

# Example 2:

# Input: "()[]{}"
# Output: true

# Example 3:

# Input: "(]"
# Output: false

# Example 4:

# Input: "([)]"
# Output: false

# Example 5:

# Input: "{[]}"
# Output: true

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        if s[0] == ']' or s[0] == '}' or s[0] == ')': 
            return False
        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            else: 
                if len(stack) == 0 or (c == ']' and stack[-1] != '['): 
                    return False
                elif len(stack) == 0 or (c == '}' and stack[-1] != '{'): 
                    return False
                elif len(stack) == 0 or (c == ')' and stack[-1] != '('): 
                    return False
                else: 
                    stack.pop()
        return len(stack) == 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid('()'))
    print(sol.isValid('()[]{}'))
    print(sol.isValid('(]'))
    print(sol.isValid('([)]'))
    print(sol.isValid('{[]}'))

# Runtime: 12 ms, faster than 98.18% of Python online submissions for Valid Parentheses.
# Memory Usage: 13 MB, less than 5.04% of Python online submissions for Valid Parentheses.