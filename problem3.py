from collections import Counter

def rearrange_by_frequency(nums):
    frequency = Counter(nums)
    rearranged = sorted(nums, key=lambda x: (-nums.count(x), x))
    return rearranged
        








print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))