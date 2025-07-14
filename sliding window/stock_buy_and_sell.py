# my solution

def maxProfit(prices: list[int]) -> int:
    buy = prices[0]
    for price in prices:
        if price < buy:
            buy = price

    i = prices.index(buy)
    future = prices[i:]

    sell = buy
    for f in future:
        if f > sell:
            sell = f

    print(sell-buy)

maxProfit([7,1,5,3,6,4])

# best solution (neetcode)

def maxProfit(prices: list[int]) -> int:
    l, r = 0, 0
    profit = 0

    while l < len(prices):
        while r < len(prices):

            if prices[l] > prices[r]:
                break

            if prices[r] - prices[l] > profit:
                profit = prices[r] - prices[l]

            r += 1
        l += 1

    return profit
maxProfit([7,1,5,3,6,4])
