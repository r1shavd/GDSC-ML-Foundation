"""
Zeros and Ones - NumPy

This code is the solution to the problem on HackerRank practice topics. Modify the code to pass all the test cases.

Author: Rishav Das (github.com/r1shavd)
"""

# Importing the required modules
import numpy

def main():
  """ The main driver function """
  # Asking the user to enter the dimension integer values
  int_list = tuple(map(int, input("Enter the dimensions: ").split()))

  # Creating the zeros and ones array using the user entered integers
  print("Zeros array: ")
  print(numpy.zeros(int_list, dtype = int))
  print("Ones array: ")
  print(numpy.ones(int_list, dtype = int))

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    exit()
  except Exception as error:
    print(f"[ Error: {error}]")
