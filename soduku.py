class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def safe(row,col,k,board): #function to check whether it is safe to insert a no. in board or not
            for i in range(9):
                if board[row][i]==k: # for checking element in same row
                    return False
                if board[i][col]==k: # for checking element in same column
                    return False
                if board[3*(row//3)+i//3][3*(col//3)+i%3]==k: # for checking element in same box
                    return False
            return True
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        for k in range(1,10):
                            k=str(k)
                            if safe(i,j,k,board):
                                board[i][j]=k
                                if solve(board):
                                    return True
                                board[i][j]='.'
                        return False # if it is not possible to insert any particular value at that cell
            return True # if all the values are filled then it will return True
        solve(board)