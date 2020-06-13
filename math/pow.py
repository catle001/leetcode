import math


def power(x, y):
    return pow_util(x, y, {})


def pow_util(x, y, dp):
    if y not in dp:
        if y == 0:
            dp[y] = 1
        elif y % 2 == 0:
            dp[y] = pow_util(x, int(y / 2), dp) * pow_util(x, int(y / 2), dp)
        else:
            dp[y] = x * pow_util(x, int(y / 2), dp) * pow_util(x, int(y / 2), dp)
    return dp[y]


def pow_bottom_up(x, y):
    if y == 0:
        return 1
    k = math.log(y, 2)
    i = 0
    result = x
    while i < k - 1:
        result *= result
        i += 1
    if y % 2 == 1:
        result *= x
    return result


def main():
    x = 2
    y = 3
    print(pow_bottom_up(x, y))


if __name__ == '__main__':
    main()
