def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    arr = [12, 11, 13, 5, 6, 7]
    new_arr = bubble_sort(arr)
    print new_arr


if __name__ == '__main__':
    main()