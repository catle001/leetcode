def selection_sort(arr):
    for i in range(len(arr)):
        min_index = find_min(arr, i)
        tmp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = tmp
    return arr

def find_min(arr, start):
    min_index = start
    for i in range(start, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index

def main():
    arr = [12, 11, 13, 5, 6, 7]
    new_arr = selection_sort(arr)
    print new_arr


if __name__ == '__main__':
    main()