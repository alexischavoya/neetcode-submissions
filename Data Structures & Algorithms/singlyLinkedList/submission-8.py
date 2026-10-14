class Node:
    def __init__(self, v, n, p):
        self.v = v
        self.n = n
        self.p = p

def getNodeOfIndex(node, index):
    # Base case: anytime we are past the last node, it doesnt count anymore
    # even if the index is 0 at that point
    if (node is None):
        return None
    # Base case: whenever the index is 0, we found the node we wanted
    if (index == 0):
        return node
    # General case: continue with the search by counting down at next node
    return getNodeOfIndex(node.n, index - 1)

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        node = getNodeOfIndex(self.head, index)

        if (node is None):
            return -1
        return node.v

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head, None)

        # Edge case: empty linked list
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
            return
        
        self.head.p = new_node
        self.head = new_node


    def insertTail(self, val: int) -> None:
        new_node = Node(val, None, self.tail)

        # Edge case: empty linked list
        if (self.tail is None):
            self.head = new_node
            self.tail = new_node
            return

        self.tail.n = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        node = getNodeOfIndex(self.head, index)

        # Case 0: node DNE
        if (node is None):
            return False
        
        # Case 1: node is head and tail
        if (node == self.head and node == self.tail):
            self.head = None
            self.tail = None
            return True
        
        # Case 2: node is head but not tail
        if (node == self.head and node != self.tail):
            next_node = self.head.n
            self.head = next_node
            next_node.p = None
            return True
        
        # Case 3: node is tail but not head
        if (node != self.head and node == self.tail):
            prev_node = self.tail.p
            self.tail = prev_node
            prev_node.n = None
            return True
        
        # Case 4: node is not tail nor head
        prev_node = node.p
        next_node = node.n
        prev_node.n = next_node
        next_node.p = prev_node
        return True


    def getValues(self) -> List[int]:
        values = []

        current_node = self.head
        while (current_node is not None):
            values.append(current_node.v)
            current_node = current_node.n
        
        return values














