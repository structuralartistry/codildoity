# fun thing is that my implementation is less code than the codility example
# and runs faster on 100k iterations
def reverse_array(arr):
  rev = []
  for index in xrange(len(arr)-1, -1, -1):
    rev.append(arr[index])
    
  return rev


#>>> cProfile.run('test_reverse_array()')
#         22000003 function calls in 8.345 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    8.345    8.345 <string>:1(<module>)
#  4000000    5.046    0.000    6.967    0.000 arrays_play.py:1(reverse_array)
#        1    1.377    1.377    8.345    8.345 arrays_play.py:8(test_reverse_array)
#  4000000    0.374    0.000    0.374    0.000 {len}
# 14000000    1.548    0.000    1.548    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def test_reverse_array():
  test_data = [
    [ [1,2,3], [3,2,1] ],
    [ [3,2,1], [1,2,3] ],
    [ [5,4,3,2,1], [1,2,3,4,5] ],
    [ ['apple', 'orange', 'pear'], ['pear', 'orange', 'apple'] ],
  ]

  for i in xrange(1000000):
    for item in test_data:
      assert reverse_array(item[0]) == item[1] 

def reverse_array_1(array):
  # get array length
  array_length = len(array)
  
  # divide array in half (index count)
  half_count = array_length//2

  # for each item on one side, exchange with the other side
  for left_item_index in xrange(half_count):
    right_item_index = array_length-left_item_index-1
 
  array[left_item_index], array[right_item_index] =  array[right_item_index], array[left_item_index]

  return array

#>>> cProfile.run('test_reverse_array_1()')
#         22000003 function calls in 8.411 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    8.411    8.411 <string>:1(<module>)
#  4000000    5.082    0.000    7.037    0.000 arrays_play.py:1(reverse_array)
#        1    1.375    1.375    8.411    8.411 arrays_play.py:35(test_reverse_array_1)
#  4000000    0.379    0.000    0.379    0.000 {len}
# 14000000    1.576    0.000    1.576    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def test_reverse_array_1():
  test_data = [
    [ [1,2,3], [3,2,1] ],
    [ [3,2,1], [1,2,3] ],
    [ [5,4,3,2,1], [1,2,3,4,5] ],
    [ ['apple', 'orange', 'pear'], ['pear', 'orange', 'apple'] ],
  ]

  for i in xrange(1000000):
    for item in test_data:
      assert reverse_array(item[0]) == item[1] 
