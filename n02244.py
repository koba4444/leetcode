class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        answer = 0
        hash = {}
        unique_task_number = 0
        for t in tasks:
            if t in hash.keys():
                if hash[t] == 1: unique_task_number -= 1
                hash[t] += 1
            else:
                hash[t] = 1
                unique_task_number += 1
        if unique_task_number > 0: return -1
        for h in hash.values():
            match h % 3:
                case 0:
                    answer += h // 3
                case 1:
                    answer += (h // 3 + 1)
                case 2:
                    answer += (h // 3 + 1)
        return answer


