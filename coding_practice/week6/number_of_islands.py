"""
Number of Islands - LeetCode #200
Using DFS to count connected components in a 2D grid.
"""
def numIslands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!="1": return
        grid[r][c]="0"
        dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)

    count=0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=="1":
                dfs(r,c)
                count+=1
    return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print("Islands:", numIslands(grid))  # Expected: 3
