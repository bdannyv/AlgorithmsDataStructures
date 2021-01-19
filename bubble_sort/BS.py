def BS(arr):
    length = len(arr)

    for i in range(length):

        for j in range(0, length - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    import random
    from timeit import default_timer as timer

    unsorted = [random.randint(0, 100) for _ in range(1000)]
    start = timer()
    BS(unsorted)
    print(f'{round(timer()-start,2)}s for my implementation')


