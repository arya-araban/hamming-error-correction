import random
from lib.useful_funcs import split, find_powers


def create_error(binary_block):
    """
    This function creates a random bit flip on binary_block (which is a list containing 0 or 1 in each cell)
    """
    rnd_idx = random.randrange(len(binary_block))
    error_block = binary_block.copy()
    error_block[rnd_idx] = 0 if error_block[rnd_idx] == 1 else 1
    return error_block


def error_detection(sent_block, received_block):
    """
    This functions detects errors by 2D parity detection
    :param sent_block: an array of bits (0 or 1)
    :param received_block: an array of bits (0 or 1)
    :return: True if error exists, False if it doesn't
    """
    k = 4

    if _parity_2d(sent_block, k) == _parity_2d(received_block, k):
        return False

    return True


def error_correction(sent_block, received_block):
    """
    this function finds the exact error in received_block by using the hamming error correction technique.
    note that this works if there's only one error.
    :return: The exact bit location of the error
    """
    pows = find_powers(len(sent_block))

    for p in pows:
        sent_block.insert(p - 1, f"p{p}")
        received_block.insert(p - 1, f"p{p}")

    sent_parities = []
    received_parities = []

    for p in pows:
        sent_pnum = []
        received_pnum = []
        for i in range(p - 1, len(sent_block), p + p):
            for j in range(i, p + i):
                if j < len(sent_block):
                    sent_pnum.append(sent_block[j])
                    received_pnum.append(received_block[j])

        sent_parities.append(0) if sent_pnum.count(1) % 2 == 0 else sent_parities.append(1)
        received_parities.append(0) if received_pnum.count(1) % 2 == 0 else received_parities.append(1)

    error_bit = 0  # the bit number where the error happened. we'll modify it and finally return it
    for i in range(len(sent_parities)):
        if sent_parities[i] != received_parities[i]:
            error_bit += 2 ** i
            print(error_bit)
    return error_bit - len(pows)


def _parity_2d(binary_block, k):
    """
    This function performs even parity checking for each chunk of binary_block
    k is the number of chunks in binary_block. note that k has to be bigger than the length of binary_block
    """
    overall_parity = []
    lsts = list(split(binary_block, k))
    # print(lsts)
    for lst in lsts:
        overall_parity.append(0) if lst.count(1) % 2 == 0 else overall_parity.append(1)
    return overall_parity
