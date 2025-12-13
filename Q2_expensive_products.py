def get_expensive_products(prices):
    return [p for p in prices if p > 100]


if __name__ == "__main__":
    prices = [120, 45, 300, 85, 150]
    print(get_expensive_products(prices))
