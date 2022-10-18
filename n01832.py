from datetime import datetime
import collections



class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        aphbt = "abcdefghijklmnopqrstuvwxyz"
        hash = {s:False for s in aphbt}
        n = len(aphbt)
        k = 0
        for s in sentence:
            if not hash[s]:
                k += 1
                hash[s] = True
                if k == n: return True
        return False


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))