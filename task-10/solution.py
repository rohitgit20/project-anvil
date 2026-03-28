def second_largest(nums):
    if len(nums) < 2:
        return -1

    unique_nums = list(set(nums))

    if len(unique_nums) < 2:
        return -1

    unique_nums.sort()
    return unique_nums[-2]