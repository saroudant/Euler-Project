"""LARGEST PRODUCT IN A GRID Problem-11
First the grid is read.
Then all the directions are taken.
Finally, for each point the product is tested in all directions. """

nb = 4

with open('grid pb11.txt',"r") as file:
    #The grid is read and transform into a matrix
    grid = file.read()
    grid = grid.split('\n')
    grid = [e.split(' ') for e in grid]
    grid = [e for e in grid if len(e) > 1]
    grid = [[int(e) for e in elt] for elt in grid]

    #Try each case
    #First the directions
    directions = [[0,1],[1,0],[1,1],[1,-1],[-1,-1],[1,1],[-1,1]]
    #Then the case
    mx = 0
    possible_x = [x for x in xrange(len(grid))]
    possible_y = [y for y in xrange(len(grid))]
    products = []
    for x in possible_x:
        for y in possible_y:
            for d in directions:
                prod = 1
                for i in xrange(nb):
                    if x + i*d[0] in possible_x and y +i*d[1] in possible_y:
                        prod *= grid[x + i*d[0]][y + i*d[1]]
                    else:
                        prod = 0
                products.append(prod)
    print max(products)