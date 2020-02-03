"""count_land
Or: Number of Islands
Coding question: Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water

A typical question which can be solved using either DFS or BFS approach
For BFS approach: if detect a land, enlarge until reach the edge, then mark the 1 to 0, using this approach will make problem pretty trivial to solve.

examples:
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
output: 1

[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

"""


def dfs(grid, row, col):
    # do boundary checks
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return
    if grid[row][col] == "0":
        return
    else:
        grid[row][col] = "0"
        # check grid ids around current
        dfs(grid, row + 1, col)
        dfs(grid, row - 1, col)
        dfs(grid, row, col + 1)
        dfs(grid, row, col - 1)
    return


def numIslands(grid):
    if grid == []: return 0
    result = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "0":
                continue
            else:
                dfs(grid, row, col)
                result += 1
    return result


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    grid2 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(numIslands(grid))
    print(numIslands(grid2))
    print(numIslands([]))
    print(numIslands([["0"]]))
    print(numIslands([["1"]]))
