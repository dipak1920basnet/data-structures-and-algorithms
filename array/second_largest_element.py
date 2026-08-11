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


# approach 2:
def second_largest(n:list[int|float])-> None| float| int:
    stack = [n[0],float("-inf")]
    for i in n:
        # if another largest exists then set (second largest to largest and largest to new largest)
        if i > stack[0]:
            stack[0], stack[1] = i, stack[0]

        # if i is greater then second largest and smaller than largest then set second largest to i
        elif i > stack[1] and i < stack[0]:
            stack[1] = i
    return stack[1]



nums = [55,32,97,-55,45,32,88,21,97]
# print(find_second_largest(nums))
print(second_largest(nums))

