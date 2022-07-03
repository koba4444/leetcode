from datetime import datetime
import re


class Solution:
    def romanToInt(self, s: str) -> int:
        s1 = s

        answer = 0
        ans_code = {1000: len(re.search(r"\AM+", s1)[0]) if re.search(r"\AM+", s1) else 0,
                    900: 1 if re.search(r"(CM)+", s1) else 0,
                    400: 1 if re.search(r"(CD)+", s1) else 0,
                    90: 1 if re.search(r"(XC)+", s1) else 0,
                    40: 1 if re.search(r"(XL)+", s1) else 0,
                    9: 1 if re.search(r"(IX)+", s1) else 0,
                    4: 1 if re.search(r"(IV)+", s1) else 0,
                    500: 1 if re.search(r"[^C]D+|\AD", s1) else 0,
                    50: 1 if re.search(r"[^X]L+|^L", s1) else 0,

                    100: len(re.search(r"C+", re.search(r"([^XC]|\A)C+($|[^CDM])", s1)[0])[0]) if re.search(r"([^CX]|\A)C+($|[^CDM])", s1) else 0,
                    10: len(re.search(r"X+", re.search(r"([^IX]|\A)X+([^LC]|$)", s1)[0])[0]) if re.search(r"([^IX]|\A)X+([^LC]|$)", s1) else 0,

                    5: 1 if re.search(r"[^I]+V|^V", s1) else 0,
                    1: len(re.search(r"I+",  re.search(r"I+[^XV]|I+$", s1)[0])[0]) if re.search(r"I+[^XV]|I+$", s1) else 0
                    }

        for key in ans_code:
            answer += ans_code[key] * key





        return (answer)

if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.romanToInt("MMMCMIV"))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))