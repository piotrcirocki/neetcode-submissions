class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_duplicate = False
        dct = {}
        for i, x in enumerate(nums):
            if x not in dct:
                dct[x] = 1
            else:
                has_duplicate = True
                return has_duplicate
        return has_duplicate
