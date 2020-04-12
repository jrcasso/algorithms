# !/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            j = i + 1
            while j <= len(nums) - 1:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
