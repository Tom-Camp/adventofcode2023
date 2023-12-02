import re

with open("files/day1", "r") as fp:
    calibrations = fp.readlines()


def get_part_b() -> int:
    total: list = []
    replace_with = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for line in calibrations:
        matches = re.findall(
            r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
        )
        if matches:
            low = matches[0] if matches[0].isdigit() else replace_with[matches[0]]
            high = matches[-1] if matches[-1].isdigit() else replace_with[matches[-1]]
        total.append((int(low) * 10) + int(high))
    return sum(total)


def get_part_a() -> int:
    total: list = []
    for lines in calibrations:
        nums = [n for n in lines if n.isdigit()]
        total.append(int(f"{nums[0]}{nums[-1]}"))
    return sum(total)


def main():
    answer_a = get_part_a()
    print(f"Part a) {answer_a}")

    answer_b = get_part_b()
    print(f"Part b) {answer_b}")


if __name__ == "__main__":
    main()
