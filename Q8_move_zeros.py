__week__ = "week2"

def move_zeroes(nums):
    last_non_zero = 0
    for current in range(len(nums)):
        if nums[current] != 0:
            nums[last_non_zero], nums[current] = nums[current], nums[last_non_zero]
            last_non_zero += 1


if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    move_zeroes(arr)
    print(arr)
