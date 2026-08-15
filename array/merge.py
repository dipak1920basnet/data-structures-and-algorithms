def Merge(arr:list, arr_2:list) -> list:
    i = 0
    j = 0
    merged_arr = []
    while i < len(arr) and j < len(arr_2):
        if arr[i] < arr_2[j]:
            merged_arr.append(arr[i])
            i += 1
        elif arr[i] > arr_2[j]:
            merged_arr.append(arr_2[j])
            j += 1
        else:
            merged_arr.append(arr[i])
            i += 1
            merged_arr.append(arr_2[j])
            j += 1

    while j < len(arr_2):
        merged_arr.append(arr_2[j])
        j +=1

    while i < len(arr):
        merged_arr.append(arr[i])
        i +=1
        
    return merged_arr


arr   = [1,2,3,4,6,7]
arr_2 = [1,2,3,4,6,7,8,9] 
print(Merge(arr, arr_2))