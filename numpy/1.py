"""
Transpose and Flatten - NumPy

Just a practice code from the problem given at HackerRank prepare section.
Edit the code to pass the test cases at HackerRank.

Author: Rishav Das (github.com/r1shavd/)
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

def main():
  """ The main driver function """
  # Asking the user for required values and setting up the array (NxM) as accordance to the user
  n, m = map(int, input("Enter the dimensions (n, m): ").split(' '))
  array1 = numpy.array([input(f"m-{i}> ").strip().split() for i in range(n)], int)

  # Displaying the transpose and flatten output on screen
  print(f"[#] Transpose: {array1.transpose()}")
  print(f"[#] Flattened array: {array1.flatten()}")

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
      exit()
  except Exception as error:
    print(f"[ Error: {error} ]")
