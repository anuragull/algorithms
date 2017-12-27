import sys
import numpy as np

def print_cost(arr, cost_matrix, x, y):
    # set the initial
    cost_matrix[0][0] = arr[0][0]
    # set the top level
    for i in range(1,x):
        cost_matrix[i][0] = arr[i][0] + cost_matrix[i-1][0]
    # set the lower level
    for i in range(1,y):
        cost_matrix[0][i] = arr[0][i] + cost_matrix[0][i-1]

    for i in range(1,x):
        for j in range(1,y):
            cost_matrix[i][j] = arr[i][j] + min(cost_matrix[i-1][j], cost_matrix[i][j-1])

    print(cost_matrix)


if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    arr = np.ones((x,y))
    cost_matrix = np.zeros((x,y))
    print_cost(arr, cost_matrix, x , y)
