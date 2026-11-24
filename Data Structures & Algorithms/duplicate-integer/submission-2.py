class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = len(set(nums))
        if unique == len(nums):
            return False
        else:
            return True