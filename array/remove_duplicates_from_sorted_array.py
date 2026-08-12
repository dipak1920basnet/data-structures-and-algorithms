def removeDuplicates(nums: list[int]) -> int:
    left = 0
    right = 1
    count = 1
    while left < right and right < len(nums):
        if nums[left]!= nums[right]:
            nums[left+1] = nums[right]
            left += 1
            count += 1
        right += 1
    return count

# using dict
def removeduplicates(nums: list[int]) -> int:
    hash_table = dict()
    for i in nums:
        hash_table[i] = hash_table.get(i,0)
    count = 0
    for i in hash_table.keys():
        nums[count] = i
        count += 1
    return count
nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,2,3]
print(removeduplicates(nums))