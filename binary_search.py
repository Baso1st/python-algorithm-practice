
def binary_search_recursive(list, value):
    return _binary_search_recursive(list, value, 0, len(list))


def _binary_search_recursive(list, value, start, end):
    if start >= end:
        return False

    mid = (start + end) // 2

    if value == list[mid]:
        return True
    elif value < list[mid]:
        return _binary_search_recursive(list, value, start, mid - 1)
    else:
        return _binary_search_recursive(list, value, mid + 1, end)
    


def binary_search_iterative(list, value):
    
    start = 0
    end = len(list)

    while start < end:
        mid = (start + end) // 2
        if value == list[mid]:
            return True
        elif value < list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return False