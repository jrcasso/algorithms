# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807
class ListNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.calculate(l1, l2)

    def calculate(self, node1, node2, carryover=0):
        if node1 or node2:
            if node1 is None:
                new_sum = node2.val + carryover
                node1_next = None
                node2_next = node2.next
            elif node2 is None:
                new_sum = node1.val + carryover
                node1_next = node1.next
                node2_next = None
            else:
                new_sum = node1.val + node2.val + carryover
                node1_next = node1.next
                node2_next = node2.next

            # The greatest significant digit gets carried over, and the least
            # significant digit gets used as the value for the current node
            if new_sum > 9:
                gsd = int(str(new_sum)[0])
                lsd = int(str(new_sum)[1])
            else:
                gsd = 0
                lsd = new_sum

            return ListNode(lsd, self.calculate(node1_next, node2_next, gsd))
        else:
            if carryover == 0:
                return None
            else:
                return ListNode(carryover, None)
