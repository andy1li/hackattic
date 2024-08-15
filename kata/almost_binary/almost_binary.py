import sys

SAMPLE_INPUT = """\
#.#.#.###.#.##.#
##.##.......#..#
#..#####..#.#...
###..#....###.##
#..#..#.#....##
#......#.##....
#############.#.""".splitlines()

SAMPLE_OUTPUT = """\
43949
55305
40744
58427
18755
16560
65530""".splitlines()


def solve(line: str) -> int:
    x = line.replace('#', '1').replace('.', '0')
    return int(x, 2)


def main():
    assert SAMPLE_OUTPUT == [str(solve(line)) for line in SAMPLE_INPUT]
    for line in sys.stdin:
        print(solve(line))


if __name__ == '__main__':
    main()
