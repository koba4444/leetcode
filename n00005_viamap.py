from datetime import datetime


def isPalindrome(s):
    return s == s[::-1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = 0
        answer = ""
        if s:
            map = {s[0]:[0]}
            l = 1
            answer = s[0]
        for cur_len in range(1, len(s)):
            if s[cur_len] in map.keys():
                for i in map[s[cur_len]]:
                    if cur_len - i + 1 > l:
                        if isPalindrome(s[i:cur_len + 1]):
                            answer = s[i:cur_len + 1]
                            l = cur_len - i + 1
            else:
                map[s[cur_len]] = []
            map[s[cur_len]].append(cur_len)

        return answer

if __name__ == "__main__":
    sol = Solution()


    start_time = datetime.now()
    print(sol.longestPalindrome("wcqdyulxbzrabuvjjouvlmbzsfpcykmmusxdgrrirljrltlnswqqgyukxjfhzhbpipkswzqroarikxtrlzjriyivdjydlfopqnbqlwiperuaeszhthcunyqejayftrlwiucvlghkurgmnlixfoaokgvucdgzscjkwleifdkjycrgwidibldabhsquotljtvjxitfyrvvwlzxavvgjkmtxswxhutxgeaajuycqpxjraxgsixtmncwauubigsxdjzmgpdwvfztuzsxwyiwjeuzapjmbpfhcdzptmcphjtzdwdlpzzqnomamykbxmsbirtxjqfylatgzzelunzgomohgmlirxkgxregmbhwpoovormmvfrhqoovewpwukfdfxlmqdcvkvjueqrkmsgraexfhdstjaxqxwfbhbuvbnyxckefikkyblrfdrsdgyjckhblycffuqfsrlsenyluxepmscukwruipanugiakyrmmvrcjsgyprrke"))
    print(sol.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(sol.longestPalindrome("wwWwwwww"))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))