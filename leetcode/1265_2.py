# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    new_list = []
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        try:
            self.printLinkedListInReverse(head.getNext())
        except:
            pass  # We have reached the last node
        finally:            
            head.printValue()
