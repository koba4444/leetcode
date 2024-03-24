from datetime import datetime
import collections


import numpy as np
class Solution:

    def isValidSudoku(self, board) -> bool:
        hash = {}
        for i in range(1,10):
            hash[str(i)] = 0
        def check_list(hash, l):
            for i in l:
                if i != '.' and hash[i] == 1:
                    return False
                elif i != '.':
                    hash[i] += 1
            for i in range(1,10):
                hash[str(i)] = 0
            return True
        def flat(l):
            if isinstance(l[0], str):
                return l
            else:
                return [l[i][j] for i in range(len(l)) for j in range(len(l[0]))]

        cols = range(9)
        rows = range(9)
        b_cols = range(3)
        b_rows = range(3)
        for i in cols:
            print(board[:][i])
            if not check_list(hash, [r[i] for r in board]):
                return False
        for i in rows:
            print(board[i][:])
            if not check_list(hash, board[i][:]):
                return False
        for i in range(3):
            for j in range(3):
                print([row[3 * j:3 * (j + 1)] for row in board[3 * i:3 * (i + 1)]])
                print(flat([row[3 * j:3 * (j + 1)] for row in board[3 * i:3 * (i + 1)]]))
                print("-----------------------")
                if not check_list(hash, flat([row[3*j:3*(j+1)] for row in board[3*i:3*(i+1)]])):
                    return False
        return True



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    board =     [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
    print(sol.isValidSudoku(board))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))