def solver(arr, n, q):
    if len(arr) < n or max(arr) > q:
        return tuple()
    sorted_arr = sorted(arr)

    result = [0] * len(arr)
    for i in range(n):
        for j in range(i, len(result), n):
            result[j] = sorted_arr.pop(0)

    return tuple(result)

arr = (3, 5, 7, 1, 6, 8, 2, 4)
n = 3
q = 13

solution = solver(arr, n, q)
print(solution)
