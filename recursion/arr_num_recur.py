def recur_arr(arr, left, right):
    if left >= right:
        return arr
    # temp_left = arr[left]
    # arr[left] = arr[right]
    # arr[right] = temp_left

    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1
    return recur_arr(arr, left, right)

arr = [0,1,2,3,4,5,6,7,8,9]

print(recur_arr(arr, 2, 6))