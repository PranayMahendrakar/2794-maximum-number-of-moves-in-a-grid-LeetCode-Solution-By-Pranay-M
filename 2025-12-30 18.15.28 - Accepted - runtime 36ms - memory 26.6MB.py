class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dp[i][j] = True if we can reach cell (i, j)
        prev = [True] * m  # all cells in first column are reachable
        
        for col in range(1, n):
            curr = [False] * m
            for row in range(m):
                val = grid[row][col]
                # Check if we can come from (row-1, col-1), (row, col-1), or (row+1, col-1)
                for dr in [-1, 0, 1]:
                    prev_row = row + dr
                    if 0 <= prev_row < m and prev[prev_row] and grid[prev_row][col-1] < val:
                        curr[row] = True
                        break
            if not any(curr):
                return col - 1
            prev = curr
        
        return n - 1