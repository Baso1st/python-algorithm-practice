import sys
from tracemalloc import start
from binary_search import binary_search_recursive, binary_search_iterative
from fibonacci import fib
import time

list = fib(100)
print('Recursive: ' + str(binary_search_recursive(list, 55)))
print('Iterative: ' + str(binary_search_iterative(list, 55)))
