#  A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
#  
#  For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.
#  
#  Write a function:
#  
#  class Solution { public int solution(int N); }
#  
#  that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
#  
#  For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.
#  
#  Assume that:
#  
#  N is an integer within the range [1..2,147,483,647].
#  Complexity:
#  
#  expected worst-case time complexity is O(log(N));
#  expected worst-case space complexity is O(1).

def solution(N):
  longest_binary_gap = 0
  current_binary_gap = 0
  one_remainder_reached = False 

  while N > 0:
    #quotient, remainder = divmod(quotient, 2)
    quotient = N // 2
    remainder = N % 2
    N = quotient # must assign after get remainder

    # until we have remainder of > 0 dont have to do the rest
    if remainder == 1: one_remainder_reached = True

    if one_remainder_reached:

      if remainder == 0:
        current_binary_gap += 1
      else:
        # remainder is 1
        if (current_binary_gap > longest_binary_gap):
          longest_binary_gap = current_binary_gap
        current_binary_gap = 0
      
  return longest_binary_gap

# using divmod:
#>>> cProfile.run('test_solution()')
#         7200003 function calls in 2.754 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    2.754    2.754 <string>:1(<module>)
#   900000    1.694    0.000    2.594    0.000 iterations_challenge.py:21(solution)
#        1    0.160    0.160    2.754    2.754 iterations_challenge.py:47(test_solution)
#  6300000    0.900    0.000    0.900    0.000 {divmod}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# using // and % alone
#>>> cProfile.run('test_solution()')
#         900003 function calls in 1.640 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    1.640    1.640 <string>:1(<module>)
#   900000    1.439    0.000    1.439    0.000 iterations_challenge.py:21(solution)
#        1    0.201    0.201    1.640    1.640 iterations_challenge.py:67(test_solution)
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def test_solution():
  for _ in xrange(0,100000):
    assert solution(7) == 0
    assert solution(28) == 0
    assert solution(9) == 2
    assert solution(529) == 4
    assert solution(20) == 1
    assert solution(15) == 0
    assert solution(1) == 0
    assert solution(2147483647) == 0
    assert solution(0) == 0
