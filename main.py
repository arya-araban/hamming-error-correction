import random
from lib.useful_funcs import split


def create_error(binary_num):
    """
    This function creates a random bit flip on binary_num (which is a list containing 0 or 1 in each cell)
    """
    rnd_idx = random.randrange(len(binary_num))
    error_num = binary_num.copy()
    error_num[rnd_idx] = 0 if error_num[rnd_idx] == 1 else 1
    return error_num


def parity_2d(binary_num, k):
    """
    This function performs even parity checking for each chunk of binary_num
    k is the number of chunks in binary_num. note that k has to be bigger than the length of binary_num
    """
    overall_parity = []
    lsts = list(split(binary_num, k))
    print(lsts)
    for lst in lsts:
        overall_parity.append(0) if lst.count(1) % 2 == 0 else overall_parity.append(1)
    return overall_parity


def error_detection(sent_num, received_num):
    k = 4
    sent_parity = parity_2d(sent_num, k)
    print(sent_parity)
    received_parity = parity_2d(received_num, k)

    if sent_parity == received_parity:
        return False

    return True
