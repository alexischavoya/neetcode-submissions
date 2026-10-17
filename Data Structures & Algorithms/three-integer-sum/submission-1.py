from collections import defaultdict

def twoSum(nums, value, value_i, indecies):
    output = set()
    for i, n in enumerate(nums):
        # skip self case
        if i == value_i:
            continue
        
        target = value - n
        for j in indecies[target]:
            if j == i or j == value_i:
                continue
            output.add(tuple(sorted([-value, target, n])))
            break
    
    return output

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # target is always 0
        # triplets must be distinct entries
        # 
        # nums guaranteed at least 3 values in it
        # nums not guaranteed a solution
        indecies = defaultdict(list)
        for i, n in enumerate(nums):
            indecies[n].append(i)
        
        output = set()

        for i, n in enumerate(nums):
            for triplet in twoSum(nums, -n, i, indecies):
                output.add(triplet)
        print(output)
        return [list(triplet) for triplet in output]