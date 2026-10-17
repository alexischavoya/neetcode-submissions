class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest_sequence = 0
        while len(s) != 0:
            # n itself is a sequence
            n = s.pop()
            sequence_length = 1

            # search before n as far as possible
            i = n-1
            while (i in s):
                s.remove(i)
                sequence_length += 1
                i -= 1
            
            # search after n as far as possible
            j = n+1
            while (j in s):
                s.remove(j)
                sequence_length += 1
                j += 1
            
            # keep sequence length if longest
            longest_sequence = max(longest_sequence, sequence_length)
        
        return longest_sequence 