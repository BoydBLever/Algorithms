# A shopkeeper sells n items where the price of the ith item is price[i]. The shopkeeper wishes to adjust the price of items such that the median of prices is exactly k. Find the minimum number of moves in which the median of prices becomes exactly K if the shopkeep can + / - 1 to the price of any item.

def getMinimumMoves(prices, k):
    n = len(prices)
    # Sorting the prices
    prices.sort()

    # Identifying the current median
    median_position = (n - 1) // 2
    current_median = prices[median_position]

    # Calculating the number of moves
    moves = abs(current_median - k)

    return moves

# Example usage
prices = [4, 2, 1, 4, 7]
k = 3
print(getMinimumMoves(prices, k))  # Output will be 1
