import time
from bubble_sort import bubble_sort


list = [*range(10000, 0, -1)]

# print(list)


sum = 0

for _ in range(5):
    list = [*range(10000, 0, -1)]
    start = time.time()
    bubble_sort(list)
    end = time.time()
    sum += (end - start)

print(sum / 5)



# print(end - start)