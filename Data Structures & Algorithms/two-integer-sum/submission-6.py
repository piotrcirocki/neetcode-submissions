class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp_lst = []
        result = []
        for i, elem in enumerate(nums):
            diff = target - elem
            if elem in tmp_lst:
                first_index = tmp_lst.index(elem)
                result =  [first_index, i]
            else:
                tmp_lst.append(diff)
        return result
        
                