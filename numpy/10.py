"""
Linear Algebra - NumPy

This is the solution to the problem at HackerRank python practice, and don't forget to modify the code to match the output in order to pass all the test cases.

Author: Rishav Das (github.com/r1shavd)
"""

# Importing the required modules
import numpy

def main():
  # Asking the user for the dimensions input
  n = int(input("Enter the dimension of the square matrix: "))
  # Asking the user for the array elements input
  array1 = numpy.array([input().split() for _ in range(n)], float)
  # Displaying the determinant of the matrix
  numpy.set_printoptions(legacy='1.13') #important
  print(numpy.linalg.det(array1))

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    exit()
  except Exception as error:
    print(f"[ Error: {error} ]")
