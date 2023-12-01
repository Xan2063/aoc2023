from Helpers import getInput
import re


def p1(data):
    lines = [x for x in data.split('\n') if x]
    return extractNumbers(lines)


def extractNumbers(lines):
    numbers = [filter(str.isdigit, s) for s in lines]
    results = [int(a + b[-1]) if b else int(a + a) for (a, *b) in numbers]
    return sum(results)


def test_example():
    data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    assert p1(data) == 142


def test_part1():
    data = getInput(1)
    assert p1(data) == 54239


def p2(data):
    lines = [x for x in data.split('\n') if x]
    d = ['one', 'two', 'three', 'four', 'five',
         'six', 'seven', 'eight', 'nine']
    pattern = re.compile("(?=(" + "|".join(d) + '))')
    replaced = [pattern.sub(lambda match: str(d.index(match.group(1)) + 1), line) for line in lines]
    return extractNumbers(replaced)


def test_part2():
    data = getInput(1)
    assert p2(data) == 55343


def test_example2():
    data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    assert p2(data) == 281
