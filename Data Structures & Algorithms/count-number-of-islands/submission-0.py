class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(row,col):
            q = deque()
            visited.add((row,col))
            q.append((row,col))

            while q:
                r,c = q.popleft()

                dirs = [[1,0], [0,1], [-1,0], [0,-1]]

                for dr, dc in dirs:
                    newRow = r + dr
                    newCol = c + dc

                    if (newRow in range(rows) and newCol in range(cols)
                        and grid[newRow][newCol] == "1"
                        and (newRow, newCol) not in visited):
                        visited.add((newRow, newCol))
                        q.append((newRow, newCol))

        for row in range(rows):
            for col in range(cols):
                if (grid[row][col] == "1" 
                    and (row,col) not in visited):
                    bfs(row,col)
                    islands += 1
        
        return islands