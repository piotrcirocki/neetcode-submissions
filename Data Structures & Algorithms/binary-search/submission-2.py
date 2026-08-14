class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_elem = 0
        max_elem = len(nums)

        def search_index(nums: list[int], target: int, minimum: int,
                         maximum: int) -> int:
            if (maximum - minimum == 0):
                return -1
            half_list = minimum + int((maximum - minimum)/2)
            element = nums[half_list]
            if element == target:
                return half_list
            else:
                if element > target:
                    min_new = 0
                    max_new = half_list
                    return search_index(nums, target, min_new, max_new)
                else:
                    min_new = half_list+1
                    max_new = maximum
                    return search_index(nums, target, min_new, max_new)
        return search_index(nums, target, min_elem, max_elem)