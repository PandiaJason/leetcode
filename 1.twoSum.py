# Brute Force
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
# print(twoSum([2,11,15,7], 9))
# print(twoSum([11,2,15,7], 9))

# Hash Map
def twoSumoN(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            # print(seen)
            return [seen[diff], i]
        seen[num] = i
# print(twoSumoN([2,11,15,7], 9))
# print(twoSumoN([11,2,15,7], 9))

# Two Pointers
def twoSumTwoPointers(nums, target):
    # Keep original indices
    i_nums = [(num, i) for i, num in enumerate(nums)]
    # print(i_nums)
    i_nums.sort()  # sort by value
    print(i_nums)

    left, right = 0, len(i_nums) - 1
    while left < right:
        s = i_nums[left][0] + i_nums[right][0]
        if s == target:
            return [i_nums[left][1], i_nums[right][1]]
        elif s < target:
            left += 1
        else:
            right -= 1
print(twoSumTwoPointers([2, 11, 15, 7], 9))
print(twoSumTwoPointers([11, 2, 15, 7], 9))
