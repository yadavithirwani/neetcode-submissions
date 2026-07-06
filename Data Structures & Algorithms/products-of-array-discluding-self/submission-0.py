import math 
class Solution:
    
    


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        # First pass - multiply with all the elements of elements to the right 
        for i in range (1,n):
            res[i] = res[i-1] * nums[i-1]

        # second pass - multiply with product of all the lements to the right 
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix*nums[i]



        return res
        