def containsDuplicate(nums: list[int]) -> bool:
    # check = dict()
    # for i in nums:
    #     try:
    #         check[i]
    #     except KeyError:
    #         check[i] = check.get(i,0)+1
    #     else:
    #         return True
    # return False


    # Solution two 
    new_check = dict()
    for k in range(len(new_check)):
        try:
            new_check[new_check[k]]
        except KeyError:
            new_check[new_check[k]] = k
        else:
            return True
    return False



print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))