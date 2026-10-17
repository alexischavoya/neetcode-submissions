class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers is non-decreasing so think: [0, 1, 1, 2, 3]
        # target guaranteed in the list
        # cant use same index (ie target 2 cant just use [1, 1])
        # also indecies should be 1 indexed for some reason
        i = 0
        j = len(numbers) - 1
        while (j > i):
            guess = numbers[i] + numbers[j]
            if (guess == target):
                break
            if (guess < target):
                i += 1
            if (guess > target):
                j -= 1
        
        return [i + 1, j + 1]
