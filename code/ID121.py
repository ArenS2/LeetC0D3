def optimus(arr):
    checkpoint = sorted(arr, reverse=True)
    if(arr == checkpoint):
        return 0
    else:
        for i in range(len(arr)):
            if(arr[i] != checkpoint[i]):
                arr = arr[i:]
                break
    high = max(arr)
    index = arr.index(high)
    profit = high - min(arr[:index+1])
    if(len(arr[index+1:]) > 1):
        profit = max(profit, optimus(arr[index+1:]))
    return profit
    
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return optimus(prices)