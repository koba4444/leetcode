from datetime import datetime
import collections


class Solution:
    def intToRoman(self, num: int) -> str:
        def get_thounds(num):
            return num // 1000

        def get_halfthounds(num):
            a = num // 500
            return a % 2

        def get_hundred(num):
            a = num // 100
            return a % 5

        def get_halfhundred(num):
            a = num // 50
            return a % 2

        def get_tens(num):
            a = num // 10
            return a % 5

        def get_fives(num):
            a = num // 5
            return a % 2

        def get_ones(num):
            return num % 5

        num_code = {"1000": get_thounds(num),
                    "500": get_halfthounds(num),
                    "100": get_hundred(num),
                    "50": get_halfhundred(num),
                    "10": get_tens(num),
                    "5": get_fives(num),
                    "1": get_ones(num)
                    }
        answer = ""
        answer += "M" * num_code["1000"]

        if num_code["100"] == 4:
            if num_code["500"] == 0:
                answer += "CD"
            else:
                answer += "CM"
        else:
            answer += "D" * num_code["500"] + "C" * num_code["100"]

        if num_code["10"] == 4:
            if num_code["50"] == 0:
                answer += "XL"
            else:
                answer += "XC"
        else:
            answer += "L" * num_code["50"] + "X" * num_code["10"]

        if num_code["1"] == 4:
            if num_code["5"] == 0:
                answer += "IV"
            else:
                answer += "IX"
        else:
            answer += "V" * num_code["5"] + "I" * num_code["1"]
        return (answer)

if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.intToRoman(3423))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))