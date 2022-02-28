
def insertion_sort(list:list):
    for i in range(1, len(list)):
        value = list[i]
        j = i - 1

        while j >= 0 and list[j] > value:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = value

