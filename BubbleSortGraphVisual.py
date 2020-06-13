"""This code plots graph for both unsorted and sorted lists for oneD.
    And for twoD, it uses matplotlib.pyplot.imshow() which a particular color  for each element in a 2X2 array.  """

'''This code requires the 'BubbleSort.py' file to be in the same directory '''

### Sahil Islam ###
### 13/06/2020 ###

from BubbleSort import *
import numpy as np
import matplotlib.pyplot as plt


def oneDVisual():
    n = int(input("Enter the length of the array: "))
    a = int(input("Enter the min  value of the elements of the array: "))
    b = int(input("Enter the max value of the elements of the array: "))
    x = np.linspace(a, b, n)
    List = np.random.randint(a, b, n)

    plt.subplot(2, 2, 1)
    plt.plot(x, List)
    plt.title("Unsorted")

    oneDSort(List)

    plt.subplot(2, 2, 4)
    plt.plot(x, List)
    plt.title("Sorted")

    plt.suptitle("Bubble Sort for 1D array\n" + "Array Length: " + str(n))
    plt.show()


def twoDVisual():
    n = int(input("Enter the side n value for (n x n) array: "))
    a = int(input("Enter the min  value of the elements of the array: "))
    b = int(input("Enter the max value of the elements of the array: "))
    List = np.random.randint(a, b, (n, n))  # A (n x n)  array of integers from 1 to n.

    plt.subplot(2, 2, 1)
    plt.imshow(List)
    plt.title("Unsorted")

    twoDSort(List)

    plt.subplot(2, 2, 4)
    plt.imshow(List)
    plt.title("Sorted")

    plt.suptitle("Bubble Sort for 2D square array\n" + "Array dimension: " + str(n) + 'X' + str(n))
    plt.show()


oneDVisual()
