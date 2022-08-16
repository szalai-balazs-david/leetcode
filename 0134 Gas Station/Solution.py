class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        difference = 0
        min_difference = 0
        index = -1
        for i in range(len(gas)):
            difference += gas[i] - cost[i]
            if difference <= min_difference:
                index = i
                min_difference = difference

        return (index + 1) % len(gas)
