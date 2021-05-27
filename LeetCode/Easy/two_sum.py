def twoSum(nums, target):
    
    for i in range(len(nums)):
        value = target - nums[i]
        if value not in nums:
            continue
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[j] == value:
                return [i, j]
    

def bruteForceTwoSum(nums, target):
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return [-1] # to check if something has gone wrong

nums = [3, 2, 4]
target = 6

print(twoSum(nums=nums, target=target))
