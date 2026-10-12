class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.pop()
                dirs = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in dirs:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and c in range(cols) and
                        grid[r][c] == "1" and (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    count += 1
        
        return count