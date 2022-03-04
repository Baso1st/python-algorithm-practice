import time
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

# sys.setrecursionlimit(1000)


############################ case 1 ###########################

# list = [*range(10000, 0, -1)]
# start = time.time()
# bubble_sort(list)
# end = time.time()

# print('bubble: ' + str(end - start) + '----' + str(list == sorted(list)))

# list = [*range(10000, 0, -1)]
# start = time.time()
# insertion_sort(list)
# end = time.time()

# print('insertion: ' + str(end - start) + '----' + str(list == sorted(list)))


list = [*range(10000, 0, -1)]
start = time.time()
merge_sort(list)
end = time.time()

print('merge: ' + str(end - start) + '----' + str(list == sorted(list)))


list = [*range(10000, 0, -1)]
start = time.time()
quick_sort(list)
end = time.time()

print('quick: ' + str(end - start) + '----' + str(list == sorted(list)))

############################ case 2 ###########################


# list1 = [*range(5000, 0, -1)]
# list2 = [*range(10000, 5000, -1)]
# list =  list1 + list2

# start = time.time()
# bubble_sort(list)
# end = time.time()

# print('bubble: ' + str(end - start) + '----' + str(list == sorted(list)))

# list1 = [*range(5000, 0, -1)]
# list2 = [*range(10000, 5000, -1)]
# list =  list1 + list2

# start = time.time()
# insertion_sort(list)
# end = time.time()

# print('insertion: ' + str(end - start) + '----' + str(list == sorted(list)))

# list1 = [*range(5000, 0, -1)]
# list2 = [*range(10000, 5000, -1)]
# list =  list1 + list2

# start = time.time()
# merge_sort(list)
# end = time.time()

# print('merge: ' + str(end - start) + '----' + str(list == sorted(list)))


# list1 = [*range(5000, 0, -1)]
# list2 = [*range(10000, 5000, -1)]
# list =  list1 + list2

# start = time.time()
# quick_sort(list)
# end = time.time()

# print('quick: ' + str(end - start) + '----' + str(list == sorted(list)))

############################ case 3 ###########################

# list = [4, 8, 3, 5, 9, 2, 1]
# quick_sort(list)
# print(list)
# print(str(list == sorted(list)))