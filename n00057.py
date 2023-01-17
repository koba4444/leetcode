from datetime import datetime
import collections


class Solution:
    def insert(self, intervals, newInterval):
        interval_to_include = [None, None]
        answer = intervals.copy()
        deleted = 0
        l = len(intervals)
        if len(intervals) == 0: return [newInterval]
        for i in range(l):
            if newInterval[0] > intervals[i-deleted][1]:
                if i == len(intervals) - 1:
                    intervals.append(newInterval)
                else:
                    continue
            else:
                if newInterval[0] <= intervals[i-deleted][0] and interval_to_include[0] == None:
                    interval_to_include[0] = newInterval[0]
                    if newInterval[1] < intervals[i-deleted][0]:
                        interval_to_include[1] = newInterval[1]
                        intervals.insert(i-deleted, [interval_to_include[0], interval_to_include[1]])
                        break
                    elif newInterval[1] <= intervals[i-deleted][1]:
                        intervals[i-deleted][0] = interval_to_include[0]
                        break
                    elif newInterval[1] > intervals[i-deleted][1]:
                        if i == l - 1:
                            intervals[i-deleted][0] = interval_to_include[0]
                            intervals[i-deleted][1] = newInterval[1]
                        else:
                            a = intervals.pop(i-deleted)
                            deleted += 1


                elif newInterval[0] <= intervals[i-deleted][0] and interval_to_include[0] != None:
                    if newInterval[1] < intervals[i-deleted][0]:
                        interval_to_include[1] = newInterval[1]
                        intervals.insert(i-deleted, [interval_to_include[0], interval_to_include[1]])
                        break
                    elif newInterval[1] <= intervals[i-deleted][1]:
                        intervals[i-deleted][0] = interval_to_include[0]
                        break
                    elif newInterval[1] > intervals[i-deleted][1]:
                        if i == l - 1:
                            intervals[i-deleted][0] = interval_to_include[0]
                            intervals[i-deleted][1] = newInterval[1]
                        else:
                            a = intervals.pop(i-deleted)
                            deleted += 1

                elif newInterval[0] <= intervals[i-deleted][1] and interval_to_include[0] == None:
                    interval_to_include[0] = intervals[i-deleted][0]
                    if newInterval[1] <= intervals[i-deleted][1]:
                        break
                    elif newInterval[1] > intervals[i-deleted][1]:
                        if i == l - 1:
                            intervals[i][0] = interval_to_include[0]
                            intervals[i][1] = newInterval[1]
                        else:
                            a = intervals.pop(i-deleted)
                            deleted += 1
                        continue
        return intervals



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.insert([[1,5],[6,8]], [0,9]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))