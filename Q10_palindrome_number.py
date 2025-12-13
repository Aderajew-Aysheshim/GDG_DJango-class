
def is_palindrome(x):
    s = str(x)
    return s == s[::-1]


if __name__ == "__main__":
    print(is_palindrome(121))
    print(is_palindrome(-121))
