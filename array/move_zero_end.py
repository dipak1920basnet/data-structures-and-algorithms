def Zero_End(nums):
    for i in range(len(nums)-1,-1,-1):
        if nums[i] == 0:
            for j in range(i,len(nums)-1):
                if nums[j+1] == 0 and  nums[j] == 0:
                    break
                nums[j+1], nums[j] = nums[j], nums[j+1]

    print(nums)

nums = [1,0,2,4,3,0,0,3,5,1]
Zero_End(nums)
# print(nums)