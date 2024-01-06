n1 = int(input().strip())
ops1 = list(map(int, (input()).strip().split(" ")))
n2 = int(input().strip())
ops2 = list(map(int, (input()).strip().split(" ")))

def current_value(ops, start_ind):
    """
    Calculates code of operation in operation list ops, number of its repetitions and next non equal code.
    :param ops:
    :param start_ind:
    :return: code, number, next_ind
    """
    ind = start_ind
    number = 0
    code = ops[start_ind]
    while ind < len(ops) and ops[ind] == code:
        number += 1
        ind += 1
    return code, number, ind


ans = []
counter1 = 0
counter2 = 0
while counter1 < n1:
    code1, number1, next_ind1 = current_value(ops1, counter1)
    while counter2 < n2 and ops2[counter2] <= code1:
        code2, number2, next_ind2 = current_value(ops2, counter2)
        if code1 == code2:
            ans.extend([str(code1)] * min(number1, number2))
        counter2 = next_ind2
    counter1 = next_ind1
print(' '.join(ans))