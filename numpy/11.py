"""
Polynomials - NumPy

This is the solution to the problem at HackerRank python practice, and don't forget to modify the code to match the output in order to pass all the test cases.

Author: Rishav Das (github.com/r1shavd)
"""

# Importing the required modules
import numpy

def main():
    print(numpy.polyval(numpy.array(tuple(map(float, input("Enter the coefficients in polynomial: ").split(' ')))), int(input("Enter the value of x: "))))

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    exit()
  except Exception as error:
    print(f"[ Error: {error} ]")
