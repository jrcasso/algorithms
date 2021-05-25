class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        pointer = 0
        cursor = self.head
        if self.head == None:
            return -1

        try:
            while pointer != index:
                cursor = cursor.next
                pointer += 1
        except AttributeError:
            # Attempting to get the value of a node at an invalid index
            return -1

        if cursor == None:
            return -1

        return cursor.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.head = Node(val, self.head)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        at_tail = False
        cursor = self.head
        if self.head == None:
            self.addAtHead(val)
            return

        while not at_tail:
            if cursor.next != None:
                cursor = cursor.next
            else:
                at_tail = True
                cursor.next = Node(val, None)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return

        try:
            pointer = 0
            cursor = self.head
            while (pointer + 1) != index:
                cursor = cursor.next
                pointer += 1

            cursor.next = Node(val, cursor.next)
        except AttributeError:
            # Attempting to add a node at an invalid index
            pass

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        try:
            if index == 0:
                self.head = self.head.next
        except AttributeError:
            # Effectively destroys the list
            self.head = None

        try:
            pointer = 0
            cursor = self.head
            while (pointer + 1) != index:
                cursor = cursor.next
                pointer += 1
            cursor.next = cursor.next.next
        except AttributeError:
            # Attempting to delete a node at an invalid index
            pass

    def printLinkedList(self):
        output = ''
        cursor = self.head
        while cursor != None:
            output += str(cursor.val)
            cursor = cursor.next
            # Lookahead to see if we need to add an arrow
            if cursor != None:
                output += ' -> '
        print(output)


obj = MyLinkedList()
obj.addAtHead(99)
obj.addAtHead(11)
obj.addAtHead(66)
obj.addAtHead(33)
obj.addAtTail(55)
obj.addAtIndex(1, 2)
obj.printLinkedList()
print("====")
obj.get(1)
obj.deleteAtIndex(1)
obj.printLinkedList()
obj.get(1)

