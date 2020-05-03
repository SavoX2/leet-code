# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Note:

# All given inputs are in lowercase letters a-z.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        # sort() is O(nlogn) worst case and O(n) best case
        strs.sort()
        output = ''
        # longest prefix can at most be the shortest word in the list
        for c in strs[0]:
            if strs[-1][:len(output) + 1] == output + c: # same as strs[-1].startswith(output + c)
                output += c
            else: 
                break
        return output

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(['flower', 'flow', 'flight']))
    print(sol.longestCommonPrefix(['dog', 'racecar', 'car']))

# Runtime: 16 ms, faster than 94.04% of Python online submissions for Longest Common Prefix.
# Memory Usage: 12.7 MB, less than 6.25% of Python online submissions for Longest Common Prefix.