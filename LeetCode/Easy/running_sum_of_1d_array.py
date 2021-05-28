
from typing import runtime_checkable


def runningSum(nums):
    r_sum = []

    for i in range(len(nums)):
        r_sum.append(sum(nums[0:i+1]))

    return r_sum

nums = [1,2,3,4]
print(runningSum(nums))