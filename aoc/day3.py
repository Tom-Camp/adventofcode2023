import re


def plot_adjacent(x: int, y: int) -> list:
    coords: list = []
    for y_coord in range(y - 1, y + 2):
        for x_coord in range(x - 1, x + 2):
            if (x_coord, y_coord) != (x, y):
                coords.append((x_coord, y_coord))
    return coords


def get_adjacent_plot() -> list:
    adjacent: list = []
    for y, line in enumerate(lines):
        for x, n in enumerate(line.strip()):
            if not n.isalnum() and n != ".":
                adjacent.extend(plot_adjacent(*(x, y)))
    return adjacent


with open("files/day3", "r") as fp:
    lines = fp.readlines()

adjacent_plot = get_adjacent_plot()


def find_parts() -> int:
    part_list: list = []
    for y, line in enumerate(lines):
        for part_number in re.finditer(r"\d+", line.strip()):
            for x in range(part_number.start(), part_number.end()):
                if (x, y) in adjacent_plot:
                    part_list.append(int(part_number.group()))
                    break
    return sum(part_list)


def main():
    parts_sum = find_parts()
    print(parts_sum)


if __name__ == "__main__":
    main()
