def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr


def main():
    arr = [12, 11, 13, 5, 6, 7]
    new_arr = insertion_sort(arr)
    print new_arr


if __name__ == '__main__':
    main()