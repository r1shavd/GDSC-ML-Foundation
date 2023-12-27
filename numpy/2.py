"""
Contenate multiple arrays - NumPy

This is the solution to the "concatenate" problem at the HackerRank prepare topics. Edit the file according to match the outputs for passing all the test cases on HackerRank.

Author: Rishav Das (github.com/r1shavd)
"""

# Importing the required modules
import numpy

def main():
  """ The main driver function """
  # Asking the user to enter values of N,M,P
  n,m,p = map(int, input("Enter the values (n,m,p): ").split(' '))

  # Asking the user to enter the array elements
  print("---- Array-1 ----")
  array1 = numpy.array([input(f"n-{i}> ").strip().split() for i in range (n)], int)
  print("----  -----  ----")
  print("---- Array-2 ----")
  array2 = numpy.array([input(f"m-{i}> ").strip().split() for i in range (m)], int)
  print("----  -----  ----")

  # Asking the user to specify the axis of the concatenation
  axis_value = int(input("Enter the axis of concatenation value: "))

  # Printing the concatenated array
  print(f"Result: {numpy.concatenate((array1, array2), axis = axis_value)}")

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    exit()
  except Exception as error:
    print(f"[ Error: {error} ]")
