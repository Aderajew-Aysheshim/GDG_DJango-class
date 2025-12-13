__week__ = "week2"

def integer_sqrt(x):
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        guess = mid * mid
        if guess == x:
            return mid
        if guess < x:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans


if __name__ == "__main__":
    print(integer_sqrt(4))
    print(integer_sqrt(8))
