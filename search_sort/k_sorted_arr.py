from heapq import heappop, heappush, heapify


def k_sort(arr, k):
    new_arr = []
    heap = arr[:k+1]
    heapify(heap)
    i = k+1
    while len(new_arr) < len(arr):
        min = heappop(heap)
        new_arr.append(min)
        if i < len(arr):
            heappush(heap, arr[i])
            i = i + 1
    return new_arr


def main():
    k = 3
    arr = [2, 6, 3, 12, 56, 8]
    new_arr = k_sort(arr, k)
    print new_arr


if __name__ == '__main__':
    main()
