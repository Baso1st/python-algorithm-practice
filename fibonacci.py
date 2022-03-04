
def fib(n):
    if n ==1:
        return 1

    list = [*range(n)]
    list[0] = list[1] = 1
    
    for i in range(2, n):
        list[i] = list[i-1] + list[i-2]

    return list