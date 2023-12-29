"""
Array Mathematics - NumPy

This is a solution to the problem at HackerRank practice problems. Modify the code accordingly to get the output to pass all the test cases.

Author: Rishav Das (github.com/r1shavd)
"""

# Importing the required modules
import numpy

def main():
  # Asking the user for the dimension inputs
  n, m = map(int, input("Enter the dimensions (n m): ").split(' '))
  # Asking the user to enter the one liner values of the matrix elements
  array1, array2 = (numpy.array([input(f"m-{i}>>> ").split() for i in range(n)], dtype=int) for _ in range(2))
  print(array1 + array2, array1 - array2, array1 * array2, array1 // array2, array1 % array2, array1 ** array2, sep = "\n")

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    exit()
  except Exception as error:
    print(f"[ Error: {error} ]")
