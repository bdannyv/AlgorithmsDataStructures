def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        for k in range(i):
            if arr[i] <= arr[k]:
                arr[i], arr[k] = arr[k], arr[i]

    return arr


def insertionSort1(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    import random
    from timeit import default_timer as timer

    array = [random.randint(0, 1000) for _ in range(1000)]
    array1 = array.copy()

    start = timer()
    insertionSort(array)
    print(f'{round(timer() - start, 2)}s for my implementation')

    start = timer()
    insertionSort1(array1)
    print(f'{round(timer() - start, 2)}s - GfGs algorithm')
