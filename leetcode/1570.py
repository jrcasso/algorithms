from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nonzero_values = {}

        for i in range(len(nums)):
            if nums[i] != 0:
                self.nonzero_values[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        for i in vec.nonzero_values:
            try:
                dot_product += vec.nonzero_values[i] * self.nonzero_values[i]
            except:
                continue
        return dot_product
