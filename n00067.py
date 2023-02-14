from datetime import datetime
import numpy as np
import collections
from functools import reduce


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str((int(a,2)+ int(b,2)).__format__("b"))





if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.addBinary("11", "1"))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))