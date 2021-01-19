import random


def mergesort(arr):
    l = len(arr)
    left = arr[:l // 2]
    right = arr[l // 2:]
    if len(left) != 1:
        left = mergesort(left)
    if len(right) != 1:
        right = mergesort(right)

    i = j = k = 0

    while j < len(left) and k < len(right):
        if left[j] <= right[k]:
            arr[i] = left[j]
            j += 1
        else:
            arr[i] = right[k]
            k += 1
        i += 1
    while j < len(left):
        arr[i] = left[j]

        j += 1
        i += 1
    while k < len(right):
        arr[i] = right[k]

        i += 1
        k += 1
    return arr


if __name__ == '__main__':
    array = [random.randint(0, 20) for i in range(10)]
    print(array)
    sorted_array = mergesort(array)
    print(sorted_array)
