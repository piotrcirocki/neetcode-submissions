class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_lst = []
        result = []
        for i, x in enumerate(nums):
            diff = target - x
            if x in temp_lst:
                first_index = temp_lst.index(x)
                result = [first_index, i]
            else:
                temp_lst.append(diff)
        return result