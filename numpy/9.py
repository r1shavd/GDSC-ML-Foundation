"""
Floor, Ceil, and Rint - NumPy

This is the solution to the problem at HackerRank python practice, and don't forget to modify the code to match the output in order to pass all the test cases.

Author: Rishav Das (github.com/r1shavd/)
"""

# Importing the required modules
import numpy

def main():
  # Asking the user for the array elements input
  array1 = numpy.array(tuple(map(float, input("Enter the array elements: ").split(' '))))

  # Displaying the results of floor, ceil, rint
  numpy.set_printoptions(legacy = "1.13")
  print(numpy.floor(array1))
  print(numpy.ceil(array1))
  print(numpy.rint(array1))

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    exit()
  except Exception as error:
    print(f"[ Error: {error} ]")
