
def merge_sort(list:list):
    if len(list) <= 1:
        return list

    middle = len(list) // 2
    L = list[: middle]
    R = list[middle:]
    
    merge_sort(L)
    merge_sort(R)

    merge_halves(list, L, R)


def merge_halves(list, L, R):
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        list[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        list[k] = R[j]
        j += 1
        k += 1