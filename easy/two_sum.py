# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup_table = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in lookup_table:
                return [lookup_table[complement], index]
            else:
                lookup_table[num] = index
        return None


if __name__ == '__main_':
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))

# Runtime: 44 ms, faster than 91.99% of Python3 online submissions for Two Sum.
# Memory Usage: 15.1 MB, less than 5.11% of Python3 online submissions for Two Sum.
