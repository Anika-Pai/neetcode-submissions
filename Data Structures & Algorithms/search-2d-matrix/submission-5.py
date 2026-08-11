class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1
        curr = -1

        while t <= b:
            m = (t + b) // 2

            if target < matrix[m][0]:
                b = m - 1
            elif target > matrix[m][-1]:
                t = m + 1
            else:
                curr = m
                break

        if curr == -1:
            return False

        for i in range(len(matrix[curr])):
            if matrix[curr][i] == target:
                return True

        return False