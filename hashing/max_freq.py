# count the element with max_frq 
def count_max(nums):
    max_freq = 0
    total_freq = 0
    freq_counter = dict()

    for num in nums:
        freq_counter[num] = freq_counter.get(num,0)+1
        freq = freq_counter[num]
        if freq > max_freq:
            max_freq = freq
            total_freq = freq
        elif freq == max_freq:
            total_freq += freq

    return total_freq

# nums = [1,2,2,3,1,4]
nums = [1,2,3,4,5]
print(count_max(nums))
        