

from datetime import datetime

LETTERS = "abcdefghigklmnopqrstuvwxyz"
DOT = "."
STAR = "*"
DOTSTAR = ".*"

def isLetterStar(s: str) -> bool:
    if len(s) == 2 and s[1] == "*" and s[0] in LETTERS:
        return True
    else:
        return False

def strConsistsOfLetters(s: str) -> bool:
    for i in s:
        if i not in LETTERS: return False
    return True

def strIsMultipleLetter(s: str, ch: str) -> bool:
    """
    returns True if s consists of just several ch
    :param s:
    :param ch:
    :return:
    """
    for i in s:
        if i != ch: return False
    return True



class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Trivial case for s consisting just one letter
        if (len(s) == 1 and s in LETTERS and ((len(p) == 1 and (s == p or p == DOT)) or (len(p) == 2 and p == DOTSTAR))):
            return True
        # Trivial case with .* pattern
        if (len(s) >= 0 and (strConsistsOfLetters(s) or s == "") and p == DOTSTAR):
            return True

        # Trivial case with "letter"* pattern
        if (len(p) == 2 and p[0] in LETTERS and p[1] == STAR and strIsMultipleLetter(s, p[0])):
            return True

        if len(s) == 0 and len(p) == 0: return True
        if len(s) > 0 and len(p) == 0: return False



        # Try to read 2 symbols from pattern
        if len(p) >= 2:
            cur_p = p[: 2]
            if cur_p == DOTSTAR:
                if len(s) == 0: return self.isMatch("", p[2:])
                if len(s) > 0:
                    k = 0
                    answer = False
                    while k <= len(s) and s[k-1] in LETTERS or k == 0:
                        answer = answer or self.isMatch(s[k:], p[2:])
                        k += 1
                    return answer


            elif isLetterStar(cur_p):  #Case of several repeating letters
                if len(s) == 0: return self.isMatch("", p[2:])
                if len(s) > 0:
                    k = 0
                    answer = False
                    while k <= len(s) and s[k-1] == p[0] or k == 0:
                        answer = answer or self.isMatch(s[k:], p[2:])
                        k += 1
                    return answer


        # Read one symbol from pattern
        if len(p) >= 1:
            if s == "": return False # Case when s is empty but pattern consists of letter
            cur_p = p[0]
            if cur_p in LETTERS:
                if cur_p != s[0]: return False
                return self.isMatch(s[1:], p[1:])
            elif cur_p == DOT:
                if not strConsistsOfLetters(s[0]): return False
                return self.isMatch(s[1:], p[1:])
            else:
                return False #wrong pattern: star without letter or dot before







if __name__ == "__main__":
    sol = Solution()

    start_time = datetime.now()
    assert(sol.isMatch("aaaab", ".*d*a*b") == True)
    assert(sol.isMatch("aaaab", "a*.*bb") == False)
    assert(sol.isMatch("aaa", "a*a") == True)
    assert(sol.isMatch("abbabaaaaaaacaa", "a*.*b.a.*c*b*a*c*") == True)
    assert(sol.isMatch("bbabaaaaaaacaa", ".*b.a.*c*b*a*") == True)
    assert(sol.isMatch("abbabaaaaaaacaa", "a*.*b.a.*c*b*a*c*") == True)
    assert(sol.isMatch("", "c*") == True)
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))

    "abbabaaaaaaacaa"
    "a*.*b.a.*c*b*a*c*"