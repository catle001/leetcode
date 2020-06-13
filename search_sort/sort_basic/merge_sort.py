def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) /2
    left_sort = merge_sort(arr[:mid])
    right_sort = merge_sort(arr[mid:])
    return combine(left_sort, right_sort)

def combine(left, right):
    arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i = i + 1
        else:
            arr.append(right[j])
            j = j + 1
    arr = arr + left[i:] + right[j:]
    return arr



def main():
    arr = [12, 11, 13, 5, 6, 7]
    new_arr = merge_sort(arr)
    print new_arr

if __name__ == '__main__':
    main()