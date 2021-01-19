def partition(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end

    while True:

        while low <= high and arr[low] <= pivot:
            low += 1

        while high >= low and arr[high] >= pivot:
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]

    return high


def quicksort(arr, start, end):
    if start >= end:
        return

    p = partition(arr, start, end)
    quicksort(arr, p + 1, end)
    quicksort(arr, start, p - 1)


if __name__ == '__main__':
    import random
    array = [random.randint(0,10) for _ in range(10)]
    print(array)
    quicksort(array, 0, len(array)-1)
    print(array)
