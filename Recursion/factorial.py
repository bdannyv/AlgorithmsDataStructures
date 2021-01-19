def factorial(num):  # num!=
    res = num
    if num > 2:
        num -= 1
        res *= factorial(num)
    return res


def test(num):
    if num == 0:
        return 0
    res = 1
    for i in range(res, num + 1):
        res *= i
    return res


if __name__ == '__main__':
    for i in range(10):
        rec = factorial(i)
        ite = test(i)
        print(f'{rec=}, {ite=}')
        print('ok' if rec == ite else 'failed')
