# method 1:
def frequency_count(nums):
    hash = dict()
    for i in nums:
        try:
            hash[i] += 1
        except KeyError:
            hash[i] = 1
    return hash

# other style

def frequency_count_two(nums):
    hash = {}
    length = len(nums)

    # One way 
    # for i in range(0, length):
    #     hash[nums[i]] = hash.get(nums[i], 0) + 1
    
    # other way
    for i in nums:
        hash[i] = hash.get(i,0)+1
    return hash

nums = [1,1,2,2,3,3,4,4,4]
print(frequency_count(nums))
print(frequency_count_two(nums))