from datetime import datetime
import collections
"""
class Trie_node():
    def __init__(self, letter, val=0, next={}):

        self.letter = letter
        self.val = val
        self.next = next

    def add_node(self, cur_tier, letter):
        if letter in cur_tier.next:
            return cur_tier.next[letter]
        else:
            cur_tier.next[letter] = Trie_node(letter)
            return cur_tier.next[letter]

    def copy(self):
        ret = Trie_node(self.letter)
        ret.val = self.val
        ret.next = self.next.copy()
        return ret
************** There is no need in Trie (( ************************
"""

class Solution:
    def topKFrequent(self, words, k: int):
        #trie = Trie_node('0')
        hash = {}

        for w in words:
            for l in w:
                pass
                #a = trie.add_node(cur_trie, l)
                #cur_trie = Trie_node(a.letter, a.val, a.next)
            if w in hash:
                hash[w] += 1
            else:
                hash[w] = 1

        hash1 = [[key, item] for key,item in hash.items()]
        hash1.sort(key=lambda x: (-x[1],x[0]))
        ans = [x[0] for x in hash1[:k]]
        return ans[:k]






if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.topKFrequent(["i","love","leetcode","i","love","coding"],2 ))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))