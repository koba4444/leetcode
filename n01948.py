from datetime import datetime
import collections

class Trie_node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = []
        self.next.append(next)

class Solution:
    def deleteDuplicateFolder(self, paths):
        global hashmap
        global trie
        trie = Trie_node("/")
        for p in paths:
            cur_trie = trie
            for nd in p:
                if nd not in cur_trie.next:
                    cur_trie.next.append(Trie_node(nd))
                else:
                    cur_trie.next = [Trie_node(nd)]


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

    print(sol.deleteDuplicateFolder([["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))