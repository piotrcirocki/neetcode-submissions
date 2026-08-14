class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        value = 0
        value0 = 0
        value1 = 0
        for i in range (len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])

            value = min(cost[0], cost[1])

        return value 
        