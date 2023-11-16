#Here is a simple task. Take an array/tuple of unique positive integers, and two additional positive integers. Here's an example below: arr = (3,5,7,1,6,8,2,4) n = 3 # span length q = 13 # weight threshold Try to re-arrange arr so that the sum of any n consecutive values does not exceed q. solver(arr,n,q) ## one possible solution: (4,7,1,5,6,2,3,8) Did you succeed? Great! Now teach a computer to do it. Technical Details All test inputs will be valid All test cases will have 0 or more possible solutions If a test case has no solution, return an empty array/tuple. Otherwise, return a valid solutio    Test constraints: 2 <= n <= 6 4 <= arr length < 12 n < arr length Every value in arr will be less than q 11 fixed tests, 25 random tests
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
