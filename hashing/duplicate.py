def containsDuplicate(nums: list[int]) -> bool:
    check = dict()
    for i in nums:
        try:
            check[i]
        except KeyError:
            check[i] = check.get(i,0)+1
        else:
            return True
    return False

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))