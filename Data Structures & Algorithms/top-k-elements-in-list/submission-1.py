class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i, x in enumerate(nums):
            if x in dct:
                dct[x] += 1
            else:
                dct[x] = 0
        sorted_values = dict(
            sorted(dct.items(), key=lambda item: item[1], reverse=True)[:k]
        )
        return list(sorted_values.keys())
