class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_duplicates = False
        dct = {}
        for num in nums:
            if num in dct:
                has_duplicates = True
                return has_duplicates
            else:
                dct[num] = True

        return has_duplicates
