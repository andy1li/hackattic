from base64 import b64decode
from struct import unpack

from utils import get_input, post_result

PROBLEM_SET = 'help_me_unpack'


def solve(input_str: str):
    decoded_bytes = b64decode(input_str)
    assert len(decoded_bytes) == 32
    int, uint, short, float, double = unpack('iIhfd', decoded_bytes[:24])
    big_endian_double = unpack('>d', decoded_bytes[24:])[0]
    return {
        'int': int,
        'uint': uint,
        'short': short,
        'float': float,
        'double': double,
        'big_endian_double': big_endian_double,
    }


def main():
    json = get_input(PROBLEM_SET)
    result = solve(json['bytes'])
    post_result(PROBLEM_SET, result)


if __name__ == '__main__':
    main()
