def most_freq(nums,k):
    freq_count = dict()
    for i in nums:
        freq_count[i] = freq_count.get(i,0)+1

    sorted_ = dict(sorted(freq_count.items(), key=lambda item: item[1], reverse=True))

    m = [key for key in sorted_.keys()][:k]
    return m 

nums = [1,1,1,2,2,3,3,3]
k = 3
# nums = [1]
# k = 1
# nums = [1,2,1,2,1,2,3,1,3,2]
# k = 2
print(most_freq(nums, k))