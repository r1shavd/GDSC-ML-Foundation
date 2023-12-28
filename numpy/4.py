"""
Eye and Identity - NumPy

This prints an identity matrix of the user entered dimensions. Solution to the problem on HackerRank practice topics.

Author: Rishav Das (github.com/r1shavd/)
"""

# Importing the required modules
import numpy
numpy.set_printoptions(legacy = "1.13")

def main():
  """ The main driver function """
  n, m = map(int, input("Enter the dimensions (n, m): ").split(' '))
  print(numpy.eye(n, m, k = 0))

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    exit()
  except Exception as error:
    print(f"[ Error: {error} ]")
