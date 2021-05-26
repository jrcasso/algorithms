# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        if head.next == None:
            return False
        slow_cursor = head
        fast_cursor = head.next

        while slow_cursor != fast_cursor:
            if fast_cursor == None or fast_cursor.next == None:
                # Reached the end of the list without cycles
                return False
            slow_cursor = slow_cursor.next
            fast_cursor = fast_cursor.next.next
        return True

    def hasCycleHashmap(self, head: ListNode) -> bool:
        if head == None:
            return False
        if head.next == None:
            return False

        seen_nodes = []
        cursor = head
        while cursor != None:
            if cursor in seen_nodes:
                return True
            else:
                seen_nodes.append(cursor)
            cursor = cursor.next
        return False

    def hasCycleIndex(self, head: ListNode) -> bool:
        if head == None:
            return None
        if head.next == None:
            return None
        slow_cursor = head
        fast_cursor = head.next
        while slow_cursor != fast_cursor:
            if fast_cursor == None or fast_cursor.next == None:
                # Reached the end of the list without cycles
                return None
            prior_cursor = slow_cursor
            slow_cursor = slow_cursor.next
            fast_cursor = fast_cursor.next.next
        return prior_cursor

