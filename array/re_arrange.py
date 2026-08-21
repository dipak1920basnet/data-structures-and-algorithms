# Approach one
def rearrangeArray(self, nums: list[int]) -> list[int]:
    positive_stack = []
    negative_stack = []

    for i in nums:
        if i >= 0:
            positive_stack.append(i)
        else:
            negative_stack.append(i)

    final_stack = []

    for j in range(len(positive_stack)):
        final_stack.append(positive_stack[j])
        final_stack.append(negative_stack[j])

    return final_stack


# Approach two:

# def RearrangeArray(self, nums: list[int]) -> list[int]:
#     array = []
#     positive_tracer = 0
#     negative_tracer = 1

#     while positive_tracer < len(nums) and negative_tracer < len(nums):
#         ...




# nums = [3,1,-2,-5,2,-4]

# RearrangeArray(nums)