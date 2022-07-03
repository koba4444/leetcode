from datetime import datetime
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        tab = []
        for i in range(numRows):
            tab.append([""])
        answer = ""
        x = 0
        y = -1
        direction = "down"
        for i in s:
            if direction == "down":
                if y + 1 < numRows:
                    tab[y + 1][x] = i
                    #print(tab)
                    y += 1
                    if y + 1 == numRows:
                        direction = "rightup"
            elif direction == "rightup":
                if y - 1 > -1:
                    for j in range(numRows):
                        tab[j].append("")
                    tab[y - 1][x+1] = i
                    #print(tab)
                    y -= 1
                    x += 1
                    if y - 1 == -1:
                        direction = "down"
        for i in range(numRows):
            for j in tab[i]:
                answer += j
        return answer



if __name__ == "__main__":
    sol = Solution()


    start_time = datetime.now()
    print(sol.convert("AB", 1))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))