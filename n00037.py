from datetime import datetime
import numpy as np
import collections
from functools import reduce

fullset = set("123456789")

class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        arr = np.array(board)
        min_blanks = 81
        def check_sudoku_board(arr):
            nonlocal min_blanks
            blanks = np.where(arr == '.')
            n = len(blanks[0])
            if n < min_blanks:
                min_blanks = n
            if len(blanks[0]) == 0:
                return arr
            else:
                mosaic_rows = [set(arr.reshape((9, 9))[i, :].flatten()) - {"."} for i in range(9)]
                mosaic_cols = [set(arr.reshape((9, 9))[:, i].flatten()) - {"."} for i in range(9)]
                mosaic_3x3square = [
                    [set(arr.reshape((9, 9))[3 * i:3 * i + 3, 3 * j:3 * j + 3].flatten()) - {"."} for j in range(3)] for
                    i
                    in range(3)]
                pretendents = (fullset -
                               mosaic_rows[blanks[0][0]] - mosaic_cols[blanks[1][0]] -
                               mosaic_3x3square[blanks[0][0] // 3][blanks[1][0] // 3]
                               )
                for i in list(pretendents):
                    arr[blanks[0][0],blanks[1][0]] = i
                    ans = check_sudoku_board(arr.copy())
                    if not ans is None:
                        return ans
                return None



            return arr
        print(id(board))
        ans = check_sudoku_board(arr).tolist()
        for i in range(9):
            for j in range(9):
                board[i][j] = ans[i][j]
        print(id(board))


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))