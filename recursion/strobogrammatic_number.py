def strobo_number(n):
    arr = []
    if n == 1:
        return [1, 8, 6, 9]
    for solution in strobo_number(n-1):
        for num in [1, 0, 8, 6, 9]:
            arr.append(solution*10 + num)
    return arr


def main():
    n = 2
    new_arr = strobo_number(n)
    print new_arr


if __name__ == '__main__':
    main()
