# A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
# 
# Your goal is to find that missing element.
# 
# Write a function:
# 
# def solution(A)
# that, given a zero-indexed array A, returns the value of the missing element.
# 
# For example, given array A such that:
# 
#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.
# 
# Assume that:
# 
# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].
# Complexity:
# 
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
# Elements of input arrays can be modified.

def solution(A):
  length = len(A)
  if length == 0:
    return 0
  elif length <= 2:
    return A[0]-1

  # initialize to highest/lowest poss values in reverse
  min_elem = 100000
  max_elem = 0

  A_sum = 0
  for i in A:
    if i < min_elem: min_elem = i
    if i > max_elem: max_elem = i
    A_sum += i

  expected_sum = 0
  for i in xrange(min_elem, max_elem+1):
    expected_sum += i

  return expected_sum - A_sum

def test_solution():
  arr = [2,3,1,5]
  assert solution(arr) == 4

  # with 0 elem
  arr = []
  assert solution(arr) == 0

  # with 1 elem
  arr = [3]
  assert solution(arr) == 2

  # with 2 elem
  arr = [3,4]
  assert solution(arr) == 2

  # large sequential
  arr = [i for i in xrange(1,100001)]
  assert len(arr) == 100000
  assert solution(arr) == 0

  # large range
  arr = [i for i in xrange(1,100001)]
  assert len(arr) == 100000
  assert arr[50000] == 50001
  del arr[50000]
  assert solution(arr) == 50001
    
