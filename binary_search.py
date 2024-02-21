def binary_search(nums, target):
    first = 0
    last = len(nums) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] < target:
            first += 1   
        else:
            last -= 1
    return None
    
nums = [1,2,3,4,5,6,7,8,9,10]
target = 2
print(binary_search(nums, target))