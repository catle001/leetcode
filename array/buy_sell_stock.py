class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float('inf')
        for current_price in prices:
            if current_price < min_price:
                min_price = current_price
            elif current_price - min_price > max_profit:
                max_profit = current_price - min_price
        return max_profit


def main():
    price =  [7,1,5,3,6,4]
    solution = Solution().maxProfit(price)
    print(solution)


if __name__ == '__main__':
    main()