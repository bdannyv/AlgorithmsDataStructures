import random


def countingSort(arr, exp):
    # index of digit to compare : 1-units, 2 - decimals etc
    exp = 10 ** (exp-1)
    n = len(arr)
    count = [0 for _ in range(10)]
    output = [None for _ in range(n)]

    for i in arr:
        index = i / exp
        count[int(index % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] / exp)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    return output


def radix_sort(arr):
    max_el = max(arr)
    pos = 1
    while max_el/(10 ** (pos-1)) >= 1:
        arr = countingSort(arr, pos)
        pos += 1

    return arr


if __name__ == '__main__':
    for _ in range(10):
        ar = [random.randint(1, 10000) for _ in range(5)]
        sorted_ar = radix_sort(ar)
        print(f'{ar=}\n{sorted_ar=}')
        print('ok' if radix_sort(ar) == sorted(ar) else 'failed')
