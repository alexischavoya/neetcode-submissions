# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        size = len(pairs)
        if (size == 0):
            return []
        if (size == 1):
            return [pairs]

        sort_steps = [pairs.copy()]

        # First element is already always sorted, i is the first unsorted item
        for i in range(1, size):
            # count down to 0 and keep swaping
            for j in range(i-1, -1, -1):
                left = j
                right = j + 1
                if (pairs[right].key < pairs[left].key):
                    pairs[left], pairs[right] = pairs[right], pairs[left]
            # store work done
            sort_steps.append(pairs.copy())
        
        return sort_steps

    def selectionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        size = len(pairs)
        if (size == 0 or size == 1):
            return [pairs]

        sort_steps = [pairs.copy()]
        for i in range(size - 1):
            # while looking at the ith element, look through all remaining future elements
            # and find the location of the smallest element
            min_j = i
            for j in range(i + 1, size):
                if (pairs[j].key < pairs[min_j].key):
                    min_j = j
            # swap the positions
            pairs[i], pairs[min_j] = pairs[min_j], pairs[i]
            sort_steps.append(pairs.copy())
        
        return sort_steps