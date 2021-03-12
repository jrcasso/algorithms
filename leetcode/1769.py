class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        solution = []
        for i in range(len(boxes)):
            moves = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    moves += abs(i - j)
            solution.append(moves)
        return solution
