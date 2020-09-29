from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        j = 0
        while j < n:
            nums.insert(2 * j + 1, nums.pop(n + j))
            j += 1
        return nums
