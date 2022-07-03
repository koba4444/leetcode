from datetime import datetime
import collections


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        l = len(s)
        sum = 0
        #if l - k + 1 < 2**k: return False
        sbin = int(s, base=2)
        hash_table = 0
        #print(hash_table)
        map = 2**k - 1
        #print(type(map), map)
        for i in range(l - k + 1):
            proxi = (1 << ((sbin>>i)&map))
            print(bin(proxi))
            hash_table = hash_table | proxi
        print("s  ", len(s), s)
        print(len(bin(map)), bin(map<<1))
        print("hash  ", len(bin(hash_table)),bin(hash_table))

        print(bin(2**(l - k + 1) - 1))
        print(len(bin(2**(l - k + 1) - 1)))
        if hash_table & (2**(l - k + 1) - 1) != (2**(l - k + 1) -1): return False

        return True




if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    "00110110"
    print(sol.hasAllCodes("00110110", 2))

    print(sol.hasAllCodes("01001000100111101001010101110100010001011100011100100101010000001101010101110100100011010110101000011111111111101000010010000001000111111001110010000001011010001110100010001010001110010111011010110101110110110011010001001000110001101010101010111011111000010110101101100010000001001110000000000001100110111001011010100101001011111110010010001100011100101110111001100101001011100001110", 7))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))