class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i, x in enumerate(nums):
            if x not in dct:
                dct[x] = i
            diff = target - x
            if diff in dct and i != dct[diff]:
                fst_idx = dct[diff]
                snd_idx = i
                return [fst_idx, snd_idx]
        return [0]