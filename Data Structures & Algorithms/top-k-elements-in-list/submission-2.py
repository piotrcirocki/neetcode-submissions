class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k is the element of top k frequesnt e.g. top 2 most frequent.
        dct = {}
        for i, x in enumerate(nums):
            if x in dct:
                dct[x] += 1
            else:
                dct[x] = 0

        nums = []
        for num, cnt in dct.items():
            nums.append([cnt, num])
        nums.sort()
        result_values = nums[-k:]
        result = []
        for i in result_values:
            result.append(i[1])
        return result