class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        c=0
        t=0
        n = len(cost)
        e = 0
        for i in range(n):
            c += gas[i] - cost[i]
            t += gas[i] - cost[i]
            if c < 0:
                c = 0
                e = (i+1)%n
        if t >= 0:
            return e
        return -1


