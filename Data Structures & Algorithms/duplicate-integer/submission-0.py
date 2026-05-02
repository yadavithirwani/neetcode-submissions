class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

        # BRUTE FORCE SOLUTION - Compare everything by itself 
        # SORTING - Onlogn memory complexity
        

         