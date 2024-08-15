import sys
from itertools import groupby

SAMPLE_INPUT = """\
aaaaaiiiixqvsm
rrdkuuuuyyyrrrrgghc
xhzzzccccvvsssqppc
jbiiiulllllvvvvtttttxxxxxs""".splitlines()

SAMPLE_OUTPUT = """\
5a4ixqvsm
rrdk4u3y4rgghc
xh3z4cvv3sqppc
jb3iu5l4v5t5xs""".splitlines()


def handle_group(group):
    x, g = group
    size = len(list(g))
    if size == 1:
        return x
    elif size == 2:
        return x * 2
    else:
        return str(size) + x


def solve(line: str) -> str:
    return ''.join(map(handle_group, groupby(line.strip())))


def main():
    assert SAMPLE_OUTPUT == [solve(line) for line in SAMPLE_INPUT]
    for line in sys.stdin:
        print(solve(line))


if __name__ == '__main__':
    main()
