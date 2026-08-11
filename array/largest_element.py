def find_largest(n:list[int|float])->int|float|None:
    # python treats empty list as false
    if not n:
        return None
    largest = n[0]
    # largest = float("-inf")
    for i in n:
        if i > largest:
            largest = i
    return largest

nums = [55,32,-97,99.99,3,67]

print(find_largest(nums))