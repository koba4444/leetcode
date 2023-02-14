from datetime import datetime
import numpy as np
import collections
from functools import reduce


class Solution:
    def totalNQueens(self, n: int):
        ans = []
        def check_places(n, curr_row, early_places=[]):
            """
            returns possible places for queens in curr_row row
            given queewns in early_places in upper rows
            """


            for i in range(n):
                i_fitted = True
                if len(early_places) > 0:
                    for pl in early_places:
                        if i == pl[1] or abs(curr_row - pl[0]) == abs(i - pl[1]):
                            i_fitted = False
                            break
                if i_fitted:
                    if n - 1 == curr_row:
                        # last queen set
                        new_early_places = early_places + [[curr_row, i]]
                        ans.append(new_early_places)
                    else:
                        # set not las queen/ next subroutine needed
                        new_early_places = early_places + [[curr_row, i]]
                        q = check_places(n, curr_row + 1, new_early_places)

                    # next queen setting not possible
            return ans
        return len(check_places(n, 0, []))





if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.totalNQueens(4))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))