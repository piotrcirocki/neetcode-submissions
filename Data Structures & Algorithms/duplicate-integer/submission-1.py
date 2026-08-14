class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        more_than_once = False
        dct = {}
        for i in nums:
            if i in dct:
                more_than_once = True
            else: 
                dct[i] = 1
        return more_than_once