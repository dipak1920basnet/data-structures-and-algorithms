def find_largest(n:list[int|float])->int|float|None:
    # python treats empty list as false
    if not n:
        # return None if the list is empty
        return None
    largest = n[0]
    # largest = float("-inf")
    for i in n:

        # check if current number is greater than available largest number
        # if yes change the largest number to current number
        if i > largest:
            largest = i

        # largest = max(i, largest)
    return largest

nums = [55,32,-97,99.99,3,67]

print(find_largest(nums))