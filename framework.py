import numpy as np

nums = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

def checkSolved(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            row = arr[i]
            col = arr[:, j]
            box = (arr[int(i / 3) * 3:(int(i / 3) + 1) * 3, int(j / 3) * 3:(int(j / 3) + 1) * 3]).flatten()
            if not (len((list(set(row) - set(nums)) + list(set(nums) - set(row))) + (
                    list(set(col) - set(nums)) + list(set(nums) - set(col))) + (
                                list(set(box) - set(nums)) + list(set(nums) - set(box)))) == 0):
                return False

    return True

def possible(arr, x, y):
    row = arr[y]
    col = arr[:, x]
    one = (list(set(nums) - set(row)) + list(set(row) - set(nums)))
    two = (list(set(nums) - set(col)) + list(set(col) - set(nums)))
    box = (arr[int(y / 3) * 3:(int(y / 3) + 1) * 3, int(x / 3) * 3:(int(x / 3) + 1) * 3]).flatten()
    three = (list(set(nums) - set(box)) + list(set(box) - set(nums)))
    combo = list(set(one) & set(two) & set(three))
    if (0 in combo):
        combo.remove(0)
    return (combo)

def possibilityList(arr):
    possibilities = np.zeros((9, 9), dtype=object)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            possibilities[i, j] = possible(arr, j, i)
    return possibilities

def createChoices():
    choices = np.zeros((9, 9), dtype=object)
    for i in range(len(choices)):
        for j in range(len(choices[0])):
            choices[i, j] = [0]
    return choices
