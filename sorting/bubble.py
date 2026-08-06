def Bubble_sort_asc(n):
    if len(n) == 0 or len(n) == 1:
        return n
    i = 1
    m = 0
    while True:
        if n[i] < n[i-1]:
            n[i-1], n[i] = n[i], n[i-1]
        i+=1
        if i >= len(n)-m:
            i = 1
            m+=1
        if m == len(n):
            break
        # for j in range(1,len(n)):
        #     if n[j] < n[j-1]:
        #         break
        # else:
        #     break
    return n 

def Bubble_sort_dsc(n):
    if len(n) == 0 or len(n) == 1:
        return n
    i = 1
    while True:
        if n[i] > n[i-1]:
            n[i-1], n[i] = n[i], n[i-1]
        i+=1
        if i >= len(n):
            i = 1

        for j in range(1,len(n)):
            if n[j] > n[j-1]:
                break
        else:
            break
    return n 

def Bubble_sort(n, reverse:bool = False):
    if reverse:
        return Bubble_sort_dsc(n)
    return Bubble_sort_asc(n)

n = [5,8,1,6,9,2,4]
# n = [2,1]
print(Bubble_sort(n))