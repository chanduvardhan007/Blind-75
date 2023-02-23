class Solution:
    def maxProfit(prices):
        #Method 1
        # q=math.inf
        # profit=0
        # for price in prices:
        #     if price < q:
        #         q=price
        #     else:
        #         if price-q > profit:
        #             profit= price-q
        # return profit
        
        #Method 2
        start=0
        end=1
        max_profit=0
        while (end < len(prices)):
            if prices[start]<prices[end]:
                profit=prices[end]-prices[start]
                max_profit=max(max_profit,profit)
            else:
                start=end
            end+=1
        return max_profit
    print(maxProfit([7,1,5,3,6,4]))