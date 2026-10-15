from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # { v : i for i, v in enumerate(nums) }
        pairs = defaultdict(list)
        for i, n in enumerate(nums):
            pairs[n].append(i)

        for i in range(len(nums)):
            pair = target - nums[i]
            if (pair in pairs.keys()):
                js = pairs[pair]
                # could be [5, 5, 5, ...] target=10
                for j in js:
                    if i != j:
                        return [i, j]
        
        # contition is guaranteed
        return []