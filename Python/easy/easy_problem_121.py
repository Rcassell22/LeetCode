class Solution(object):

    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

        Used GPT for this since my own was too slow.
        For prompting, I just showed it my slow code, and asked how I could optimize it.
        It told me to get rid of the nested loops (duh), and gave me this function.

        This is almsot exactly what I had done previously with JS so I don't feel too bad.
        """
        if not prices or len(prices) < 2:
            return 0

        min_price = max(prices)
        max_profit = 0

        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


    def max_profit_reuben(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


        This was my solution, it works, but it is too slow for LeetCode.

        See max_profit for "my" GPT optimized solution.
        """
        current_profit = 0

        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                # need to skip prices we know won't return a profit, otherwise it's way too slow
                if prices[j] <= prices[i]:
                    break
                working_profit = prices[j] - prices[i]
                current_profit = max(working_profit, current_profit)
                j += 1
            i += 1
        return current_profit