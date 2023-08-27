class Solution :
    def get_row_col(self,matrix) :
        for r in range(5) :
            for c in range(5) :
                if matrix[r][c] == 1 :
                    return r,c
    def minimum_steps(self,matrix) ->int :
        row,col = self.get_row_col(matrix)
        visited = set()

        def dfs(r,c,visited) :
            if (r,c) in visited :
                return float("inf")
            if r >= 5 or r < 0 or c >= 5 or c < 0 :
                return float("inf")
            if matrix[r][c] == 1 and r == 2 and c == 2 :
                return 0
            visited.add((r,c))
            left_col,left_row,right_row,right_col = float("inf"),float("inf"),float("inf"),float("inf")

            #swap with left row
            if r >= 1 :
                matrix[r-1][c] , matrix[r][c] = matrix[r][c],matrix[r-1][c]
                left_row = dfs(r-1,c,visited) + 1
                matrix[r-1][c] , matrix[r][c] = matrix[r][c],matrix[r-1][c]
            #swap with right row
            if r < 4 :
                matrix[r+1][c] , matrix[r][c] = matrix[r][c],matrix[r+1][c]
                right_row = dfs(r+1,c,visited) + 1
                matrix[r+1][c] , matrix[r][c] = matrix[r][c],matrix[r+1][c]
            #swap with left col
            if c >= 1 :
                matrix[r][c-1] , matrix[r][c] = matrix[r][c],matrix[r][c-1]
                left_col = dfs(r,c - 1,visited) + 1
                matrix[r][c - 1] , matrix[r][c] = matrix[r][c],matrix[r][c-1]
            if c < 4 :
                matrix[r][c+1] , matrix[r][c] = matrix[r][c],matrix[r][c+1]
                right_col = dfs(r,c + 1,visited) + 1
                matrix[r][c + 1] , matrix[r][c] = matrix[r][c],matrix[r][c + 1]

            visited.remove((r,c))
            return min(left_col,left_row,right_col,right_row)
        return dfs(row,col,visited)

'''
Taking a 5x5 matrix as input
'''
mat = []
for i in range(5) :
    row = list(map(int,input().split()))
    mat.append(row)
obj = Solution()
print(obj.minimum_steps(mat))