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
  n = len(A)+1
  
  actual_sum = 0
  expected_sum = n*((n+1))/2
  for i in A:
    actual_sum += i

  return expected_sum-actual_sum

def test_solution():
  arr = [2,3,1,5]
  assert solution(arr) == 4

  # with 0 elem
  arr = []
  assert solution(arr) == 1

  # with 1 elem
  arr = [1]
  assert solution(arr) == 2

  # with 2 elem
  arr = [1,2]
  assert solution(arr) == 3

  # large sequential
  arr = [i for i in xrange(1,100001)]
  assert len(arr) == 100000
  assert solution(arr) == 100001

  # large range
  arr = [i for i in xrange(1,100001)]
  assert len(arr) == 100000
  assert arr[50000] == 50001
  del arr[50000]
  assert solution(arr) == 50001
    
