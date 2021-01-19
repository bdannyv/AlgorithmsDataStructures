import random


def binary_search(array, l, r, x):
    if r >= l:

        mid = l + (r - l) // 2

        if array[mid] == x:
            return mid

        elif array[mid] > x:
            return binary_search(array, l, mid-1, x)

        else:
            return binary_search(array, mid+1, r, x)
    else:
        return -1


def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1

if __name__ == '__main__':
    arr = [i for i in range(10)]

    for _ in range(20):
        num = random.randint(0, 100)

        try:
            builtin = arr.index(num)
        except ValueError:
            builtin = -1
        func = binary_search(arr, 0, len(arr)-1, num)

        print('ok' if func == builtin else 'failed')
