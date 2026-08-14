def Right_rotate(nums:list,k) -> list:
    # item = nums.pop()
    # nums.insert(0,item)
    # print(nums)
    # # # method two 
    # # print(nums[-k:] + nums[:-k])
    arr_len = len(nums)

    while k > arr_len:
        k -= arr_len

    # if arr_len == 0 or arr_len == 1 or arr_len == k or k == 0:
    #     return nums

    # return nums[:k] + nums[k:]
    return nums[arr_len-k:] + nums[:arr_len-k]
    # return nums

# nums = [5,-2,3,9,0,6,10,7]
nums = [1,2,3,4,5,6,7]
k = 3
print(Right_rotate(nums, k))