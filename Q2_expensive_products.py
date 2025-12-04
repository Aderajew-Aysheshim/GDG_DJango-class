def get_expensive_products(prices):
    result = []
    for price in prices:
        if price > 100:
            result.append(price)
    return result

prices = [120, 45, 300, 85, 150]
print(get_expensive_products(prices))
