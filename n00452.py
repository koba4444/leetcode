class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        l = len(points)
        points.sort(key=(lambda x: x[1]) )

        if l == 0: return 0
        answer = 1
        curr_i = 0
        for i in range(1, len(points)):
            if points[i][0] > points[curr_i][1]:
                curr_i = i
                answer += 1
        return answer