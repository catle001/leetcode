def quick_sort(arr):
    if len(arr) < 2:
        return arr
    low, high = partition(arr, arr[-1])
    return quick_sort(low) + [arr[-1]] + quick_sort(high)


def partition(arr, pivot):
    low = []
    high = []
    for i in range(len(arr) - 1):
        if arr[i] >= pivot:
            high.append(arr[i])
        else:
            low.append(arr[i])
    return low, high


def main():
    arr = [12, 11, 13, 5, 6, 7]
    new_arr = quick_sort(arr)
    print new_arr


if __name__ == '__main__':
    main()
