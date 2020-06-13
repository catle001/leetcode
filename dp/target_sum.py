def dp(arr, total, i, mem, solution_arr):
    key = str(total) + ':' + str(i)
    if key in mem:
        return mem[key] + solution_arr
    if total == 0:
        return solution_arr
    elif total < 0:
        return []
    elif i<0:
        return []
    elif total < arr[i]:
        to_return = dp(arr, total, i-1, mem, solution_arr)
    else:
        to_return = []
        include = dp(arr, total-arr[i], i-1, mem, solution_arr + [arr[i]])
        non_include = dp(arr, total, i-1, mem, solution_arr)
        if len(include) is not 0:
            to_return = to_return + [include]
        if len(non_include) is not 0:
            to_return = to_return + [non_include]
    mem[key] = to_return
    print "mem[" + str(key) + "]= " + str(mem[key])
    return to_return

def main():
    mem ={}
    arr = [2,4,6,10]
    total = 16
    print dp(arr, total, len(arr)-1, mem, [])
    # arr = [].append(1)
    # print arr

if __name__ == '__main__':
    main()