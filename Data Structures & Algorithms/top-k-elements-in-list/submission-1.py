from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        return [n for n,c in sorted(freq.items(), key=lambda item : -item[1])[:k]]