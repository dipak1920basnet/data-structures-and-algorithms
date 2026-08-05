def Selection_Sort(n:list):
    min_idx = 0
    for i in range(len(n)):
        min_idx = i
        print(min_idx)
        for j in range(i, len(n)):
            if n[j] < n[min_idx]:
                min_idx = j
                print(min_idx)
        else:
            n[i], n[min_idx] = n[min_idx], n[i]
    return n 


def Descending_Selection_sort(n:list):
    min_idx = 0
    for i in range(len(n)):
        min_idx = i
        print(min_idx)
        for j in range(i, len(n)):
            if n[j] > n[min_idx]:
                min_idx = j
                print(min_idx)
        else:
            n[i], n[min_idx] = n[min_idx], n[i]
    return n 

n = [5,7,8,4,1,6,8,2]
# print(Selection_Sort(n))
print(Descending_Selection_sort(n))