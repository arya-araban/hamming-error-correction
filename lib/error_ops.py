import random
from lib.useful_funcs import split, find_powers


def create_error(binary_num):
    """
    This function creates a random bit flip on binary_num (which is a list containing 0 or 1 in each cell)
    """
    rnd_idx = random.randrange(len(binary_num))
    error_num = binary_num.copy()
    error_num[rnd_idx] = 0 if error_num[rnd_idx] == 1 else 1
    return error_num


def error_detection(sent_num, received_num):
    k = 4

    if _parity_2d(sent_num, k) == _parity_2d(received_num, k):
        return False

    return True


def error_correction(sent_num, received_num):
    # this function finds the error in received_num (difference between sent and received) and corrects it

    pows = find_powers(len(sent_num))

    for p in pows:
        sent_num.insert(p - 1, f"p{p}")
        received_num.insert(p - 1, f"p{p}")

    sent_parities = []
    received_parities = []

    for p in pows:
        sent_pnum = []
        received_pnum = []
        for i in range(p - 1, len(sent_num), p + p):
            for j in range(i, p + i):
                if j < len(sent_num):
                    sent_pnum.append(sent_num[j])
                    received_pnum.append(received_num[j])

        sent_parities.append(0) if sent_pnum.count(1) % 2 == 0 else sent_parities.append(1)
        received_parities.append(0) if received_pnum.count(1) % 2 == 0 else received_parities.append(1)

    error_bit = 0  # the bit number where error happened. we'll modify it and finally return it
    for i in range(len(sent_parities)):
        if sent_parities[i] != received_parities[i]:
            error_bit += 2 ** i

    return error_bit - len(pows)


def _parity_2d(binary_num, k):
    """
    This function performs even parity checking for each chunk of binary_num
    k is the number of chunks in binary_num. note that k has to be bigger than the length of binary_num
    """
    overall_parity = []
    lsts = list(split(binary_num, k))
    # print(lsts)
    for lst in lsts:
        overall_parity.append(0) if lst.count(1) % 2 == 0 else overall_parity.append(1)
    return overall_parity


print(error_correction([1, 0, 0, 1, 1, 0, 1, 0], [1, 0, 0, 1, 1, 0, 1, 0]))
