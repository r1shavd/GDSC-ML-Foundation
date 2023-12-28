"""
Min and Max - NumPy

This is the solution to the problem at HackerRank practice topics, and change the code accordingly to match the output for passing all the test cases.

Author: Rishav Das (github.com/r1shavd)
"""

# Importing the required modules
import numpy

def main():
  # Asking the user for dimensions input
  n, m = map(int, input("Enter the dimensions (n m): ").split(' '))
  # Asking the user for array values
  array1 = numpy.array([ input(f"m-{i}>>> ").strip().split() for i in range(n) ], int)
  array1 = numpy.min(array1, axis = 1)
  print(numpy.max(array1))

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    exit()
  except Exception as error:
    print(f"[ Error: {error} ]")
