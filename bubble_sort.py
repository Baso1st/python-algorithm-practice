
def bubble_sort(list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list) - 1):
            j = i + 1
            if list[i] > list[j]:
                swap(list, i, j)
                swapped = True


def swap(list: list, i, j):
    list[i], list[j] =  list[j], list[i]