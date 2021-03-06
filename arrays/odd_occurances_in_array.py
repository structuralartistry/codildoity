# A non-empty zero-indexed array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.
# 
# For example, in array A such that:
# 
#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the elements at indexes 0 and 2 have value 9,
# the elements at indexes 1 and 3 have value 3,
# the elements at indexes 4 and 6 have value 9,
# the element at index 5 has value 7 and is unpaired.
# Write a function:
# 
# int solution(int A[], int N);
# that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.
# 
# For example, given array A such that:
# 
#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the function should return 7, as explained in the example above.
# 
# Assume that:
# 
# N is an odd integer within the range [1..1,000,000];
# each element of array A is an integer within the range [1..1,000,000,000];
# all but one of the values in A occur an even number of times.
# Complexity:
# 
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
# Elements of input arrays can be modified.


# this uses hash for non-matches
# was concerned that using hash would take me out of O(n) time but this solution scored 100%
def solution(array):
  non_matches_hash = {}

  array_length = len(array)
  for i in xrange(array_length):
    val = array[i]

    existing_value = non_matches_hash.get(val)
    if existing_value == None:
      non_matches_hash[val] = 1
    else:
      # remove val from hash as there is a match now
      del non_matches_hash[val]

  return non_matches_hash.keys()[0]

def test_solution():
  A = [9,3,9,3,9,7,9]

  arr1 = []
  arr1 = [1000000000 for _ in xrange(999998)]
  arr1 += [8]
  assert len(arr1) == 999999
  assert arr1[len(arr1)-1] == 8

  arr2 = []
  arr2 = [i for i in xrange(400000)]
  arr2 += [1000000000]
  arr2 += [i for i in xrange(400000)]
  assert len(arr2) == 800001
  assert arr2[400000] == 1000000000

  assert solution(A) == 7
  assert solution(arr1) == 8
  assert solution(arr2) == 1000000000


# VERY SLOW
# this uses array for non-matches
def solution_1(array):
  non_matches_array = []

  array_length = len(array)
  for i in xrange(array_length):
    val = array[i]
    # find/see if val exists in non-matches array
    existing_value = False
    for j in xrange(len(non_matches_array)):
      if non_matches_array[j] == val:
        existing_value = True
        del non_matches_array[j]
        break

    if existing_value == False:
      # add to non-matches array
      non_matches_array += [val]

  return non_matches_array[0]

# VERY SLOW
def solution_2(array):
  # spec is up to 1m elements in list
  # is None faster?
  lookup_array = [None for _ in xrange(1000000000)]
  matches_array = []

  array_length = len(array)
  for i in xrange(array_length):
    val = array[i]
    existing_value_index = lookup_array[val-1]
    if existing_value_index == None:
      # zero index, so val-1
      lookup_array[val-1] = i
    else:
      # add match to matches array
      matches_array += [val] * 2
      # remove from lookup array as pair already matched
      lookup_array[val-1] = None # reset count

  return list(set(array) - set(matches_array))[0]
