class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = None
        maximum = None
        for item in prices:
            if minimum == None or minimum > item:
                minimum = item
            elif maximum == None or maximum < item - minimum:
                maximum = item - minimum
        if maximum == None or minimum == None:
            return 0
        return maximum
