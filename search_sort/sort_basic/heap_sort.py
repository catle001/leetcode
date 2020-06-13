def heap_sort(arr):
    heapify(arr, len(arr))
    for i in range(1, len(arr)):
        arr[0], arr[-i] = arr[-i], arr[0]
        heapify(arr, len(arr) - i)
    return arr


def heapify(arr, len):
    for i in range(len / 2 - 1, -1, -1):
        left = i * 2 + 1
        right = i * 2 + 2
        largest = i
        if left < len and arr[left] > arr[largest]:
            largest = left
        if right < len and arr[right] > arr[largest]:
            largest = right
        arr[i], arr[largest] = arr[largest], arr[i]
    return arr


def main():
    arr = [12, 11, 13, 5, 6, 7]
    new_arr = heap_sort(arr)
    print new_arr


if __name__ == '__main__':
    main()
