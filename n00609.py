from datetime import datetime
import collections


class Solution:
    def findDuplicate(self, paths):
        global hashmap
        hashmap = {}
        ans = []

        def add_to_hashmap(path):
            chunks = path.split()
            for ind, ch in enumerate(chunks):
                if ind > 0:
                    cont_parts = ch.split('(')
                    content = ch.split('(')[1][:-1]
                    if cont_parts[1][:-1] in hashmap:
                        hashmap[content].append(chunks[0] + '/' +cont_parts[0])
                    else:
                        hashmap[content] = [chunks[0] + '/' + cont_parts[0]]

        for p in paths:
            add_to_hashmap(p)

        for h in hashmap:
            if len(hashmap[h]) > 1:
                ans.append(hashmap[h])
        return ans



if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))