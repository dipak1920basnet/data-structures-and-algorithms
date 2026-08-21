# Approach one
# def rearrangeArray(nums: list[int]) -> list[int]:
#     positive_stack = []
#     negative_stack = []

#     for i in nums:
#         if i >= 0:
#             positive_stack.append(i)
#         else:
#             negative_stack.append(i)

#     final_stack = []

#     for j in range(len(positive_stack)):
#         final_stack.append(positive_stack[j])
#         final_stack.append(negative_stack[j])

#     return final_stack


# Approach two:

def RearrangeArray(nums: list[int]) -> list[int]:
    array = [0]*len(nums)
    pos = 0
    neg = 1
    for i in range(len(array)):
        if nums[i] >= 0:
            array[pos] = nums[i]
            pos += 2
        else:
            array[neg] = nums[i]
            neg += 2
    print(array)

nums = [3,1,-2,-5,2,-4]

RearrangeArray(nums)