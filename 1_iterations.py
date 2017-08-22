# content of test_sample.py
def inc(x):
  return x + 1

def test_answer():
  assert inc(3) == 4

# for loops
def for_1():
  output = [] 
  for i in range(0, 100):
    output.append(i)
  return output

def test_for_1():
  assert len(for_1()) == 100

def factorial(n):
  factorial = 1
  for i in range(1, n):
    factorial += factorial * i
    print "i: {0}, factorial: {1}".format(i, factorial)
  return factorial
  #>>> cProfile.run('factorial(1000)')
  #         4 function calls in 0.001 seconds
  #
  #   Ordered by: standard name
  #
  #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #        1    0.001    0.001    0.001    0.001 1_iterations.py:18(factorial)
  #        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
  #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  #        1    0.000    0.000    0.000    0.000 {range}

# note using *= makes this faster than ^
def factorial_codility(n):
  factorial = 1
  for i in range(1, n+1):
    factorial *= i
    print "i: {0}, factorial: {1}".format(i, factorial)
  return factorial
  #>>> cProfile.run('factorial_codility(1000)')
  #         4 function calls in 0.000 seconds
  #
  #   Ordered by: standard name
  #
  #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #        1    0.000    0.000    0.000    0.000 1_iterations.py:24(factorial_codility)
  #        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
  #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  #        1    0.000    0.000    0.000    0.000 {range}

def test_factorial():
  assert factorial(1) == 1
  assert factorial(2) == 2
  assert factorial(10) == 3628800

