def minPrice(prices: list[int], discounts: list[int]) -> float:
    prices = sorted(prices)
    discounts = sorted(discounts)
    for i in range(1,len(prices)+1):
        try:
            prices[-i] *= ((100 - discounts[-i])/100)
        except IndexError:
            break
    return sum(prices)

# prices = [10,30,21]
# discounts = [50,60]

prices = [100,70]
discounts = [10,40,50]

print(minPrice(prices, discounts))