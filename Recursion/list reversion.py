from timeit import default_timer as timer


def reverse(l):
    result = [l.pop()]
    if l:
        result += reverse(l)
    return result


if __name__ == '__main__':
    start = timer()
    for k in range(10, 20):
        l = [i for i in range(k)]
        rev = reverse(l)
        test = [i for i in range(k-1, -1, -1)]
        print('ok' if rev == test else 'FAILED')
    print(f'execution time is {timer() - start}s')
