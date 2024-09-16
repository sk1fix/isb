import math
import mpmath

from paths import JSON_PATH, TEST_RESULTS, PI
from functions import read_json, write_to_file


def frequency_test(sequence: str) -> float:
    """
    This function gets possibility for the frequency bit test

    Parametres:
        sequence (str): sequence of bytes

    Returns:
        float: P value
    """
    try:
        n = len(sequence)
        one_c = sequence.count("1")
        zero_c = n - one_c
        s = abs(one_c-zero_c) / math.sqrt(n)
        p = math.erfc(s / math.sqrt(2))
        return p
    except Exception as ex:
        print("ALL BAD")


def identical_bit_test(sequence: str) -> float:
    """
    This function gets possibility for the identical bits in a sequence

    Parametres:
        sequence (str): sequence of bytes

    Returns:
        float: P value
    """
    try:
        n = len(sequence)
        one_c = sequence.count("1") / n
        if abs(one_c - 0.5) > 2 / math.sqrt(n):
            return 0.0
        v = 0
        for i in range(n - 1):
            if sequence[i] != sequence[i + 1]:
                v += 1
        p = mpmath.erfc(abs(v - 2 * n * one_c * (1 - one_c)) /
                        (2 * math.sqrt(2 * n) * one_c * (1 - one_c)))
        return p
    except Exception as ex:
        print("ALL BAD")


def longest_subsequence(sequence: str) -> float:
    """
    This function gets possibility for the longest sequence of ones in a block

    Parametres:
        sequence (str): sequence of bytes    
    Returns:
        float: P value
    """
    try:
        block_length = 8
        v = {1: 0, 2: 0, 3: 0, 4: 0}
        hi = 0
        for block_start in range(0, len(sequence), block_length):
            block = sequence[block_start: block_start + block_length]
            max_length, length = 0, 0
            for bit in block:
                if bit == "1":
                    length += 1
                    max_length = max(max_length, length)
                else:
                    length = 0
            match max_length:
                case 0 | 1:
                    v[1] += 1
                case 2:
                    v[2] += 1
                case 3:
                    v[3] += 1
                case _:
                    v[4] += 1
        for i in range(4):
            hi += ((v[i + 1] - 16 * PI[i])**2 / (16 * PI[i]))
        p = mpmath.gammainc(3 / 2, hi / 2)
        return p
    except Exception as ex:
        print("ALL BAD")


if __name__ == "__main__":
    sequences = read_json(JSON_PATH)
    cpp = sequences["cpp"]
    java = sequences["java"]
    write_to_file(TEST_RESULTS, str(frequency_test(cpp)) + " cpp\n")
    write_to_file(TEST_RESULTS, str(identical_bit_test(cpp)) + " cpp\n")
    write_to_file(TEST_RESULTS, str(longest_subsequence(cpp)) + " cpp\n")
    write_to_file(TEST_RESULTS, str(frequency_test(java)) + " java\n")
    write_to_file(TEST_RESULTS, str(identical_bit_test(java)) + " java\n")
    write_to_file(TEST_RESULTS, str(longest_subsequence(java)) + " java\n")
