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


def longest_binary_gap(binary_num):
  first_one_reached = 0 
  max_gap_length = 0
  current_gap_length = 0

  word_length = len(binary_num)

# 00000 shouldn't find any... how?
# strip leading/tailing 0
#   - dont ch curr len to max length if no 1 yet
#   - dont ch curr len to max length if ends on 0

  # start at second and end second to last char 
  for i in xrange(0, word_length):
    if binary_num[i] == '0':
      current_gap_length += 1

    # if at end of word and the value is 0 we dont want to count this gap length
    if i == word_length-1:
      current_gap_length = 0
    else:
      if first_one_reached == 0:
        current_gap_length = 0
      first_one_reached = 1
      if (current_gap_length > max_gap_length) & first_one_reached == 1:
        max_gap_length = current_gap_length
      current_gap_length = 0

  # this handles 
  if first_one_reached == 0:
    current_gap_length = 0
  if (current_gap_length > max_gap_length) & first_one_reached == 1:
    max_gap_length = current_gap_length
  return max_gap_length

def test_longest_binary_gap():
  assert longest_binary_gap('10001') == 3
  assert longest_binary_gap('11011') == 1
  assert longest_binary_gap('11001') == 2

  assert longest_binary_gap('00001') == 0

  assert longest_binary_gap('00000') == 0
  assert longest_binary_gap('11111') == 0
  assert longest_binary_gap('10000') == 0



