"""count_land
Or: Number of Islands
Coding question: Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water

A typical question which can be solved using either DFS or BFS approach
For BFS approach: if detect a land, enlarge until reach the edge, then mark the 1 to 0, using this approach will make problem pretty trivial to solve.
"""