""" PATH SUM : TWO WAYS - Problem 81

Very basic and simple version. Recursivity is used and solution
are stored so that exponential curse is broken.
"""

def max_path(grid,i,j,grid_sum):
    """
    If the value has already been computed, then this value is returned
    , otherwise it is computed by looking at the minimum value and calling
    the function back recursively
    :param grid: List of values
    :param i: Where the algorithm is (vertical)
    :param j: Where the algorithm is (horizontal)
    :param grid_sum: Values previously computed.
    :return:
    """
    if grid_sum[i][j] != 0:
        return grid_sum[i][j]
    elif i == len(grid) - 1 and j == len(grid[0]) - 1:
        grid_sum[-1][-1] = grid[-1][-1]
        return grid[-1][-1]
    elif j == len(grid[0]) - 1:
        grid_sum[i][j] = grid[i][j] + max_path(grid,i+1,j,grid_sum)
        return grid[i][j] + max_path(grid,i+1,j,grid_sum)
    elif i == len(grid) - 1:
        grid_sum[i][j] = grid[i][j] + max_path(grid,i,j+1,grid_sum)
        return grid[i][j] + max_path(grid,i,j+1,grid_sum)
    else:
        grid_sum[i][j] = grid[i][j] + min(max_path(grid,i,j+1,grid_sum),max_path(grid,i+1,j,grid_sum))
        return grid[i][j] + min(max_path(grid,i,j+1,grid_sum),max_path(grid,i+1,j,grid_sum))



with open("grid pb81.txt","r") as grid:
    #The matrix is read.
    grid = grid.read()
    grid = grid.split('\n')
    grid = [e.split(',') for e in grid if e != '']
    grid = [[int(val) for val in line] for line in grid]

    #grid = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,496,121,956],[805,732,524,37,331]]
    grid_sum = [[0 for i in row] for row in grid]
    grid_sum[-1][-1] = grid[-1][-1]


    print max_path(grid,0,0,grid_sum)
