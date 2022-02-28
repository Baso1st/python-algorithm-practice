import time
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

# case 1: 
# list = [*range(10000, 0, -1)]
# start = time.time()
# bubble_sort(list)
# end = time.time()

# print('bubble: ' + str(end - start))

# list = [*range(10000, 0, -1)]
# start = time.time()
# insertion_sort(list)
# end = time.time()

# print('insertion: ' + str(end - start))


# list = [*range(10000, 0, -1)]
# start = time.time()
# merge_sort(list)
# end = time.time()

# print('merge: ' + str(end - start))


# case 2 
list1 = [*range(5000, 0, -1)]
list2 = [*range(10000, 5000, -1)]
list =  list1 + list2

start = time.time()
bubble_sort(list)
end = time.time()

print('bubble: ' + str(end - start))

list1 = [*range(5000, 0, -1)]
list2 = [*range(10000, 5000, -1)]
list =  list1 + list2

start = time.time()
insertion_sort(list)
end = time.time()

print('insertion: ' + str(end - start))


list1 = [*range(5000, 0, -1)]
list2 = [*range(10000, 5000, -1)]
list =  list1 + list2

start = time.time()
merge_sort(list)
end = time.time()

print('merge: ' + str(end - start))


# list = [9, 5, 4, 4, 2, 1, 8, 6, 7, 3]
# merge_sort(list)
# print(list)