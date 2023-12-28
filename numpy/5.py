"""
Sum and Product - NumPy

This is the solution to the problem at HackerRank practice topics, and modify the code accordingly for the desired output to pass all the test cases.

Author: Rishav Das (github.com/r1shavd)
"""

# Importing the required modules
import numpy

def main():
    # Asking the user to enter the values of dimensions NxM
    n, m = map(int, input("Enter the dimensions (n m): ").split(' '))
    # Asking the user for array values
    array1 = numpy.array([ input(f"m-{i}>>> ").strip().split() for i in range(n) ], int)
    
    # Calculating the sum and product of that and displaying the output to the user
    array1 = numpy.sum(array1, axis = 0)
    print(numpy.prod(array1, axis = None))
    del array1

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
    except Exception as error:
        print(f"[ Error: {error} ]")
