class Solution:
    def topKFrequent(self,    nums: List[int], k: int) -> List[int]:
            kelements = []
            elems = {}
            for i, x in enumerate(nums):
                if x in elems:
                    elems[x] += 1
                else:
                    elems[x] = 1
            sortedelems = sorted(elems.items(), key=lambda k: k[1], reverse=True)
            kfirst = sortedelems[0:k]
            second_elemens = [x[0] for x in kfirst]
            return second_elemens
