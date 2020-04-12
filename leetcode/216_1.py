import itertools

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Combination brute-force approach:
        # Initialize a set of sets called "solutions"
        #
        # Pick k combinations from all possible elements
        # Take the sum of all elements in the set.
        # If the sum is n, add to solutions
        # Return solutions
        solutions = []

        for combo in itertools.combinations(range(1, 10), k):
            if sum(combo) == n:
                solutions.append(list(combo))

        return solutions
