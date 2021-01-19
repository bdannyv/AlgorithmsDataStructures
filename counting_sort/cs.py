import random


def counting_sort(int_array):
    is_numerical = True
    if type(int_array[0]) == str:
        is_numerical = False
        int_array = [ord(i) for i in int_array]
    end = max(int_array)
    l = len(int_array)

    count = [0 for _ in range(end + 1)]

    for i in int_array:
        count[i] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [None for _ in range(l)]

    for item in int_array:
        output[count[item] - 1] = item
        count[item] -= 1
    if not is_numerical:
        output = [chr(i) for i in output]

    return output


if __name__ == '__main__':
    for _ in range(10):
        ar = [random.randint(65, 75) for _ in range(20)]
        print('ok' if counting_sort(ar) == sorted(ar) else 'failed')
