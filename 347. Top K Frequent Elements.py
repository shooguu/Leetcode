import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = dict()
        for item in nums:
            if item not in f:
                f[item] = 1
            else:
                f[item] += 1

        return heapq.nlargest(k, f.keys(), key=f.values)
