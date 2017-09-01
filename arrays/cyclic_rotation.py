# A zero-indexed array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is also moved to the first place.
# 
# For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]. The goal is to rotate array A K times; that is, each element of A will be shifted to the right by K indexes.
# 
# Write a function:
# 
# def solution(A, K)
# that, given a zero-indexed array A consisting of N integers and an integer K, returns the array A rotated K times.
# 
# For example, given array A = [3, 8, 9, 7, 6] and K = 3, the function should return [9, 7, 6, 3, 8].
# 
# Assume that:
# 
# N and K are integers within the range [0..100];
# each element of array A is an integer within the range [-1000..1000].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

import pdb
def solution(A,K):
  N = len(A)
  # empty array case 
  if not A: return A
  
  # if will loop more than once then make K the offset, full cycles don't matter
  if N<K:
    full_cycle_times = K//N
    K = K - (full_cycle_times*N)
    
  # non-cyclding returns original array 
  if K==0 or N==K: return A 

  # rearrange
  back_end = A[-K:]
  front_end = A[0:N-K]

  return back_end + front_end


def test_solution():
  assert solution([],0) == []
  assert solution([],100) == []
  assert solution([3,8,9,7,6],5) == [3,8,9,7,6]
  assert solution([3,8,9,7,6],3) == [9,7,6,3,8]
  assert solution([3,8,9,7,6],6) == [6,3,8,9,7]
  assert solution([3,8,9,7,6],15) == [3,8,9,7,6]
  assert solution([3,8,9,7,6],18) == [9,7,6,3,8]
  assert solution([3,8,9,7,6],51) == [6,3,8,9,7]

  # N = 100
  arr = [i for i in xrange(1,101)]
  result = solution(arr, 10)
  assert result[0] == 91
  assert result[99] == 90
  result = solution(arr, 100)
  assert result[0] == 1
  assert result[99] == 100
  # N = 99 
  arr = [i for i in xrange(1,100)]
  result = solution(arr, 10)
  assert result[0] == 90
  assert result[98] == 89

