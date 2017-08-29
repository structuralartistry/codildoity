def reverse_array(arr):
  rev = []
  for index in xrange(len(arr)-1, -1, -1):
    rev.append(arr[index])
    
  return rev

def test_reverse_array():
  test_data = [
    [ [1,2,3], [3,2,1] ],
    [ [3,2,1], [1,2,3] ],
    [ [5,4,3,2,1], [1,2,3,4,5] ],
    [ ['apple', 'orange', 'pear'], ['pear', 'orange', 'apple'] ],
  ]

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

def test_reverse_array_1():
  test_data = [
    [ [1,2,3], [3,2,1] ],
    [ [3,2,1], [1,2,3] ],
    [ [5,4,3,2,1], [1,2,3,4,5] ],
    [ ['apple', 'orange', 'pear'], ['pear', 'orange', 'apple'] ],
  ]

  for item in test_data:
    assert reverse_array(item[0]) == item[1] 
