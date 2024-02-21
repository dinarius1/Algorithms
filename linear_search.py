def linear_search(nums, target):
    for i in range(0, len(nums)):
        if nums[i] == target:
            print(i)
            return i
    return None

def verify(index):
    if index is not None:
        print('Target found, the target - ', index)
    else:
        print('Target is not found')

num = [1,2,3,4,5]
target = 4

res = linear_search(num, target)
verify(res)
