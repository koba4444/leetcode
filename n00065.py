from datetime import datetime
import numpy as np
import collections
from functools import reduce
from math import factorial

class Solution:
    def isNumber(self, s: str) -> bool:
        allowences = {
            ".": True,
            "-+": True,
            "0123456789": True,
            "Ee": False,
            "mantissa": True,
            "number_body": False,
            "before_point": True,
            "mantissa_filled": False,
            "order_filled": True,
        }
        for i in s:
            if not i in "0123456789.+-eE": #symbols allowed
                return False
            if i in ".":
                if allowences["."] == False:
                    return False
                else:
                    if allowences["mantissa"] == False: #no dots allowed in order part of number
                        return False
                    if allowences['before_point'] == False: #just one dot in number allowed
                        return False
                    allowences['-+'] = False
                    allowences['before_point'] = False
                    allowences['number_body'] = True
                    allowences["."] = False

            if i in "-+":
                if allowences["-+"] == False:
                    return False
                else:
                    allowences["-+"] = False
                    allowences['number_body'] = True
                    allowences['before_point'] = True

            if i in "0123456789":
                if allowences["0123456789"] == False:
                    return False
                else:

                    allowences["-+"] = False
                    allowences['number_body'] = True
                    allowences["mantissa_filled"] = True
                    if allowences["mantissa"] == True:
                        allowences["Ee"] = True

                    if allowences["mantissa"] == False:
                        allowences["order_filled"] = True

            if i in "eE":
                if allowences["Ee"] == False:
                    return False
                else:
                    allowences["-+"] = True
                    allowences["."] = False
                    allowences['number_body'] = False
                    allowences['before_point'] = True
                    allowences["Ee"] = False
                    allowences["order_filled"] = False
                    allowences["mantissa"] = False


        if allowences["mantissa_filled"] and allowences["order_filled"]: # digits are necessary
            return True
        else:
            return False






if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.isNumber("e0"))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))