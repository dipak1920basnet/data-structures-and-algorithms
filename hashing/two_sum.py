def twoSum(nums,target):
    dicts = dict()
    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in dicts:
            return [i, dicts[diff]]
        dicts[nums[i]] = i

    
    return dicts
    
# print(twoSum([2,7,11,15],9))

# nums = [3,2,4]
# target = 6
# print(twoSum(nums, target))

print(twoSum([3,3],6))