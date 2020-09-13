


"""

Rotate an array by X items [E]. For example,A = [1,2,3,4,5,6] and X = 2, Result = [5,6,1,2,3,4]Hint​: Use 
same trick we used in "Reverse Words of a Sentence"

"""



def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def reverser(arr, start, end):
    low = start
    high = end

    while low < high:
        swap(arr, low, high)
        high -= 1
        low += 1


def rotate(arr, x):
    x = x % len(arr)

    reverser(arr, 0, len(arr) - 1)
    reverser(arr, 0, x - 1)
    reverser(arr, x, len(arr) - 1)

    return arr

print(rotate([1,2,3,4, 5, 6], 2))






