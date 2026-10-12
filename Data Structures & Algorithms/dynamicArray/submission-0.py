"""
Constraints imposed by Alexis Chavoya

- Cannot just be a list wrapper, treat [] as fixed size array
"""
class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.utilization = 0
        self.array = [None] * self.capacity


    def get(self, i: int) -> int:
        # assume i is within range of capacity
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        # assume i is within range of capacity
        self.array[i] = n


    def pushback(self, n: int) -> None:
        # check if we need to resize
        if (self.utilization >= self.capacity):
            self.resize()

        # Base case where we don't need to resize
        self.array[self.utilization] = n
        self.utilization += 1



    def popback(self) -> int:
        # assume array not empty
        self.utilization -= 1
        return self.array[self.utilization]
 

    def resize(self) -> None:
        # must re-copy to another array per self imposed constraints
        new_array = [None] * self.capacity * 2
        for i,e in enumerate(self.array):
            new_array[i] = e
        self.array = new_array
        self.capacity = self.capacity * 2



    def getSize(self) -> int:
        return self.utilization
        
    
    def getCapacity(self) -> int:
        return self.capacity
