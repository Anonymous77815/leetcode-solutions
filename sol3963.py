class Solution(object):
    def createGrid(self, m, n):
        grid = []

        for i in range(m):
            row = []
            for j in range(n):
                row.append("#")
            grid.append(row)

        grid[0][0], grid[m-1][n-1] = ".", "."

        for k in range(1, n):
            grid[0][k] = "."

        for a in range(1, m-1):
            grid[a][n-1] = "."

        return ["".join(row) for row in grid]