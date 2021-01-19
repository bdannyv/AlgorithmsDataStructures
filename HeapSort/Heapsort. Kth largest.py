import random


def heapify(arr, size, ni):
    largest = ni
    lc = ni * 2 + 1
    rc = ni * 2 + 2

    if lc < size and arr[lc] > arr[largest]:
        largest = lc

    if rc < size and arr[rc] > arr[largest]:
        largest = rc

    if largest != ni:
        arr[ni], arr[largest] = arr[largest], arr[ni]

        heapify(arr, size, largest)


def kth_largest(arr, k):
    n = len(arr)
    # Creating max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # swapping
    for i in range(n-1, n-k-1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr[n-k]


if __name__ == '__main__':
    array = [random.randint(0, 100) for i in range(10)]
    kth = kth_largest(array, 4)
    print(array)
    print(kth)
