from datetime import datetime


def isPalindrome(s):
    s1 = s[::-1]
    if s1 == s: return True
    else: return False



def findNewPalindromeLongerL(s: str, ch: str, l:int) -> str:
    b = s + ch
    answer = ""
    l_answer = 0
    for i in range(l, len(s) + 1):
        if isPalindrome(b[-i-1:]) and i >= l:
            answer = b[-i-1:]
            l_answer = i + 1
    if answer: return answer, l_answer
    else: return None, None

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = 0
        answer = ""
        if s:
            answer = ""
            l = 0
        for cur_len in range(len(s)):
            ans, l_answer = findNewPalindromeLongerL(s[:cur_len], s[cur_len], l)
            if ans:
                answer = ans
                l = l_answer
        return answer

if __name__ == "__main__":
    sol = Solution()


    start_time = datetime.now()
    print(sol.longestPalindrome("wcqdyulxbzrabuvjjouvlmbzsfpcykmmusxdgrrirljrltlnswqqgyukxjfhzhbpipkswzqroarikxtrlzjriyivdjydlfopqnbqlwiperuaeszhthcunyqejayftrlwiucvlghkurgmnlixfoaokgvucdgzscjkwleifdkjycrgwidibldabhsquotljtvjxitfyrvvwlzxavvgjkmtxswxhutxgeaajuycqpxjraxgsixtmncwauubigsxdjzmgpdwvfztuzsxwyiwjeuzapjmbpfhcdzptmcphjtzdwdlpzzqnomamykbxmsbirtxjqfylatgzzelunzgomohgmlirxkgxregmbhwpoovormmvfrhqoovewpwukfdfxlmqdcvkvjueqrkmsgraexfhdstjaxqxwfbhbuvbnyxckefikkyblrfdrsdgyjckhblycffuqfsrlsenyluxepmscukwruipanugiakyrmmvrcjsgyprrke"))
    print(sol.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(sol.longestPalindrome("wwwWwwwwwwww"))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))