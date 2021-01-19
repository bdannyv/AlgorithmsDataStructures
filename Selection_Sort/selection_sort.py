def selectionSort(arr):
    sorted_arr = []

    while arr:
        min_index = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i

        sorted_arr.append(arr.pop(min_index))

    return sorted_arr


def stolen(A):
    # Traverse through all array elements
    for i in range(len(A)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

                # Swap the found minimum element with
        # the first element
        A[i], A[min_idx] = A[min_idx], A[i]

    return A


if __name__ == '__main__':
    import random
    from timeit import default_timer as timer
    array = [random.randint(0, 1000) for _ in range(5000)]
    array1 = array.copy()

    start = timer()
    selectionSort(array)
    print(f'{round(timer()-start,2)}s for my implementation')

    start = timer()
    stolen(array1)
    print(f'{round(timer() - start, 2)}s - GfGs algorithm')
