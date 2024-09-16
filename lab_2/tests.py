import math

from paths import JSON_PATH, TEST_RESULTS
from functions import read_json, write_to_file


def frequency_test(sequence: str) -> float:
    try:
        n = len(sequence)
        one_c = sequence.count("1")
        zero_c = n - one_c
