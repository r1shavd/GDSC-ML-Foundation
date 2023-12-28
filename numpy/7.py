"""
Mean, Var, Std - NumPy

This is the solution to the problem at HackerRank practice topics, make sure to edit the code in accordance to the output to pass all the test cases.

Author: Rishav Das (github.com/r1shavd)
"""

# Importing the required modules
import numpy

def main():
  # Asking the user for the input
  n, m = map(int, input(f"Enter the dimensions (n m): ").split(' '))
  # Asking the user for array values
  array1 = numpy.array([ input(f"m-{i}>>> ").strip().split() for i in range(n) ], int)
  # Printing the mean, var, std of the array
  print(numpy.mean(array1, axis = 1))
  print(numpy.var(array1, axis = 0))
  numpy.set_printoptions(legacy = "1.13")
  print(numpy.std(array1))

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    exit()
  except Exception as error:
    print(f"[ Error: {error} ]")
