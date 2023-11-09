#We have an array of unique elements. A special kind of permutation is the one that has all of its elements in a different position than the original. Let's see how many of these permutations may be generated from an array of four elements. We put the original array with square brackets and the wanted permutations with parentheses.  A total of 9 permutations with all their elements in different positions than arr The task for this kata would be to create a code to count all these permutations for an array of certain length. Features of the random tests: l = length of the array 10 ≤ l ≤ 5000 See the example tests. Enjoy it!
from math import factorial

def count(arr):
    total_permutations = factorial(len(arr))
    special_permutations = total_permutations // 2

    return special_permutations
arr = [1, 2, 3, 4]
result = count(arr)
print(result)
