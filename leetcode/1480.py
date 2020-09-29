from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        sums = []
        for i in nums:
            running_sum += i
            sums.append(running_sum)
        return sums
