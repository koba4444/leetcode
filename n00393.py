from datetime import datetime
import collections


class Solution:
    def validUtf8(self, data):

        pattern= {
            0: (0,0,7),
            6: (1,2,5),
            14: (2,2,4),
            30: (3,2,3)
        }
        i = 0
        while i < len(data):
            inpattern = False
            for ind, p in pattern.items():
                if (data[i] >> p[2]) == ind:
                    inpattern = True
                    for k in range(p[0]):
                        i += 1
                        if i >= len(data): return False
                        if (data[i] >> 6) != 2:
                            return False
            i += 1
            if not inpattern:
                return False
        return True



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.validUtf8([197,130,1]))
    print(sol.validUtf8([235,140,4]))
    print(sol.validUtf8([237]))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))