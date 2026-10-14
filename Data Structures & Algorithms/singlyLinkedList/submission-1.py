"""
I think this is the intended implementation. If given during an interview they may not allow
the solution i gave last submission since its a doubly linked list
"""
class Node:
    def __init__(self, v, n):
        self.v = v
        self.n = n

def getIndexNode(node, index):
    # Base case: if we ever reach none, we went too far
    if (node == None):
        return None
    # Base case: if we ever reach 0, we are at the node
    if (index == 0):
        return node
    # General case: continue searching
    return getIndexNode(node.n, index - 1)

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        node = getIndexNode(self.head, index)
        return node.v if node is not None else -1


    def insertHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node

        # Edgecase: Correct for empty list
        if self.tail == None:
            self.tail = node
        

    def insertTail(self, val: int) -> None:
        node = Node(val, None)
        
        # Edgecase: list was originally empty
        if (self.tail == None):
            self.head = self.tail = node
            return
        
        # General case: add to and reassign tail
        self.tail.n = node
        self.tail = node
        

    def remove(self, index: int) -> bool:
        # Edgecase: list is empty
        if (self.head is None):
            return False
        ### Assert self.head is not None, size minimum of 1
        
        # Edgecase: list has one element
        if (self.head == self.tail):
            if (index != 0):
                return False
            self.head = self.tail = None
            return True
        ### Assert size minimum of 2
        
        # Edgecase: index is 0
        if (index == 0):
            self.head = self.head.n
            return True
        ### Assert index > 0
        
        # General case: find item prev to index
        curr = self.head
        target_index = index - 1
        while (curr is not None):
            # identify target
            if (target_index == 0):
                # if item to remove was tail, reset tail
                if (curr.n == self.tail):
                    self.tail = curr
                # delete item
                curr.n = curr.n.n
                return True
            # iterate to next node
            target_index -= 1
            curr = curr.n
        
        return False

    def getValues(self) -> List[int]:
        values = []

        curr = self.head
        while (curr is not None):
            values.append(curr.v)
            curr = curr.n

        return values

















