from lib.error_ops import *


def main():
    binary_block = [1, 0, 0, 1, 0, 1]
    errored_block = [1, 0, 0, 1, 0, 1]

    print(binary_block)
    print(errored_block)
    if error_detection(binary_block, errored_block):
        print("Error detected, locating with error correction..")
        error_bit = error_correction(binary_block, errored_block)
        print(f"error happened on bit {error_bit}")
    else:
        print("No Error detected!")


if __name__ == "__main__":
    main()
