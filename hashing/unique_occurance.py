def U_Q(nums):
    freq = dict()
    for i in nums:
        freq[i] = freq.get(i, 0)+1

    # sorted_freq = dict(sorted(freq.items(), key=lambda item:item[1]))

    prev_value = 0
    for key, value in freq.items():
        if value != prev_value:
            prev_value = value
        else:
            return False
    return True
arr = [1,2,2,1,1,3]
arr = [1,2]
arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(U_Q(arr))