class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Case 0: if more than two zeros, there results are always all zeros
        zeros = sum(1 for n in nums if n == 0)
        if zeros > 1:
            return [0] * len(nums)
        
        # Case 1: with one zero, everything is 0 except that one index
        if zeros == 1:
            product = 1
            zero_index = 0
            for i, n in enumerate(nums):
                if n == 0:
                    zero_index = i
                else:
                    product *= n
            output = [0] * len(nums)
            output[zero_index] = product
            return output

        # Case 2: no zeros, for every ith value multiple everything before with everything after
        aug = [1] + nums + [1]
        product_forward = 1
        product_backward = 1
        for i in range(len(aug)):
            product_backward *= aug[i]

        output = []
        for i in range(1, len(aug)-1):
            n = aug[i]
            product_backward //= n
            output.append(product_forward * product_backward)
            product_forward *= n
        
        return output