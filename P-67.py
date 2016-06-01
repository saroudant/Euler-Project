"""MAXIMUM PATH SUM II Problem-67
* First the grid is parsed to have it in the form of a list of lists.
* Then it recursively gives the value by giving the maximum of the two underlying
sums. In order to save some iteration time, calculated value are saved into the adj
parameter."""

def maximum_grid(g,depth,abs,adj):
    if depth == len(g) - 1:
        adj[-1][abs] = g[-1][abs]
        return g[-1][abs]
    else:
        if adj[depth+1][abs] == 0:
            adj[depth+1][abs] = maximum_grid(g,depth+1,abs,adj)

        if adj[depth+1][abs+1] == 0:
            adj[depth+1][abs+1] = maximum_grid(g,depth+1,abs+1,adj)

        adj[depth][abs] = g[depth][abs] + max(adj[depth+1][abs],adj[depth+1][abs+1])
        return adj[depth][abs]

with open("grid pb67.txt","r") as file:
    grid = file.read()
    grid = grid.split('\n')
    grid = [elt.split(' ') for elt in grid]
    grid = grid[:-1]
    grid = [[int(x) for x in elt] for elt in grid]

    adj = [[0 for x in elt] for elt in grid]
    print maximum_grid(grid,0,0,adj)