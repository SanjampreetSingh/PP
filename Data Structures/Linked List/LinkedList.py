class LinkedListNode:
    def __init__(self, data, nextNode=None) -> None:
        self.data = data
        self.nextNode = nextNode


class LinkedList:
    """
    Linked list is a linear data structure but is non contiguous in nature.
    """
    def __init__(self, head=None) -> None:
        self.head = head

    # insert node at end
    def insertNodeAtEnd(self, data) -> None:
        node = LinkedListNode(data)
        if self.head is None:
            self.head = node
            return
        else:
            currentNode = self.head
            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
            currentNode.nextNode = node

    # delete node at start
    def deleteNodeAtStart(self) -> None:
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head = self.head.nextNode

    # print Linked List
    def printLinkedList(self) -> None:
        if self.head is None:
            print("Linked list is empty")
        else:
            currentNode = self.head
            while currentNode.nextNode is not None:
                print(currentNode.data, end=" -> ")
                currentNode = currentNode.nextNode
            print("None")
