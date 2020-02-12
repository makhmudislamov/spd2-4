"""
Linked List Problems:
* Given a singly-linked list, find the middle item in the list.
* Given a singly-linked list, reverse the order of the list by modifying the nodes’ links.
* Given a linked list, rearrange the elements by interleaving the first half of the linked list with the second half.
Example: If the given linked list is A → B → C → D → E → F → G → H, nodes should be rearranged so the list becomes A → C → E → G → B → D → F → H.
* Rotate a given linked list counter-clockwise by k nodes, where k is a given integer.
Example: If the given linked list is A → B → C → D → E → F and k is 4, nodes should be modified so the list becomes E → F → A → B → C → D.
Assumptions: k is positive and smaller than n, the length of the linked list.
* Given an array of k linked lists, each of whose items are in sorted order, 
  combine all nodes (do not create new nodes) into a single linked list with all items in order.
"""


class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

### do not modify this class, or any of the methods in it, other than length()
### you may insert new methods if you like


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def append(self, data):
        if self.empty():
            self.head = LinkedNode(data)
            self.tail = self.head
        else:
            new_node = LinkedNode(data)
            self.tail.next = new_node
            self.tail = new_node

    def extend(self, array):
        for element in array:
            self.append(element)

  # implement this method
  # return the length of the linked list, an integer value
    def length(self):
        ll_len = 1
        curr_node = self.head
        if self.empty():
            return 0
        while curr_node.next != None:
            curr_node = curr_node.next
            ll_len += 1
        return ll_len
