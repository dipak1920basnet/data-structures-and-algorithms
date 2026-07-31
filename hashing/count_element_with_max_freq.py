def count_max(nums):

    # track count 
    total = 0

    # track the current max value 
    current_value = 0

    # dict that counts the frequency
    freq_count = dict()

    for i in nums:
        # count frequency
        freq_count[i] = freq_count.get(i,0)+1

    # sort the dict in 
    sorted_ = dict(sorted(freq_count.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_.items():
        # check if higer frequency count is found
        if value > current_value:
            total = value
            current_value = value
        # except for the first one check if other value are equal then add them 
        elif value == current_value:
            total += value
        # since values are sorted if equal or higher values arent found then exit the loop 
        else:
            break

    return total

nums = [1,2,2,3,1,4]
# nums = [1,2,3,4,5]
print(count_max(nums))
