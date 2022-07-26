
def quick_sort(list: list):
    _quick_sort(list, 0, len(list) - 1)


def _quick_sort(list, left, right):
    if right <= left:
        return

    index = partition(list, left, right)

    if left < index -1:
        _quick_sort(list, left, index - 1)
    if index < right:
        _quick_sort(list, index, right)


def partition(list: list, left, right):
    piviot = list[(right + left) // 2]

    while left <= right:

        while list[left] < piviot:
            left += 1

        while list[right] > piviot:
            right -= 1

        if left <= right:
            list[left], list[right] = list[right], list[left]
            left += 1
            right -= 1

    return left


if __name__ == '__main__':
    arr = [1, 2, 0, 0]
    quick_sort(arr)
    print(arr)
