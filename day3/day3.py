
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import numpy as np

DATA_FILE = 'data.txt'

with open(DATA_FILE, 'r') as f:
    local_area_array = [line for line in f]

def clean_local_area_array(array):
    clean_array_of_strings = [i.strip('\n') for i in array]
    matrix = []
    curr_array = []
    for s in clean_array_of_strings:
        for char in s:
            if char == '.':
                curr_array.append(0)
            else:
                curr_array.append(1)
        matrix.append(curr_array)
        curr_array = []
    return matrix

matrix = clean_local_area_array(local_area_array)
matrix = np.array(matrix)

def sled(matrix, inc=None):
    """ Sled Path or How many trees on the way? """
    if inc is None:
        inc = [3, 1]
    curr_col = 0
    curr_row = 0
    trees = 0
    for i in range(len(matrix)):
        try:
            if matrix[curr_row][curr_col] == 1:
                trees += 1
                # print(f'Row: {curr_row}',
                #       f'\nColumn: {curr_col}')
            curr_col += inc[0]
            curr_row += inc[1]
            if curr_col > 30:
                curr_col = 0 + (curr_col - 31)
        except IndexError:
            pass
    return trees

all_slopes = [[1, 1],
              [3, 1],
              [5, 1],
              [7, 1],
              [1, 2]]

all_trees = [sled(matrix, inc=slope)
             for slope in all_slopes]

from functools import reduce

print(reduce(lambda x, y: x*y, all_trees))