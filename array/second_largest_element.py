def find_second_largest(n:list[int|float])-> None| float| int:
    if not n:
        return None

    largest = float("-inf")
    second_largest = largest

    for i in n:
        if i > largest:
            largest = i

    for j in n:
        if j > second_largest and j < largest:
            second_largest = j

    return second_largest

nums = [55,32,97,-55,45,32,88,21]
print(find_second_largest(nums))