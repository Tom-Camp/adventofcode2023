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


def get_all_parts() -> tuple[list, dict]:
    part_sum: list = []
    part_list: dict = {}
    for y, line in enumerate(lines):
        for part_number in re.finditer(r"\d+", line.strip()):
            for x in range(part_number.start(), part_number.end()):
                if (x, y) in adjacent_plot:
                    for part_x in range(part_number.start(), part_number.end()):
                        if part_x not in part_list:
                            part_list[part_x] = {
                                y: {
                                    "part": part_number.group(),
                                    "range": (
                                        y,
                                        part_number.start(),
                                        part_number.end(),
                                    ),
                                }
                            }
                        else:
                            part_list[part_x][y] = {
                                "part": part_number.group(),
                                "range": (y, part_number.start(), part_number.end()),
                            }
                    part_sum.append(int(part_number.group()))
                    break
    return part_sum, part_list


def get_gears(parts: dict) -> list:
    all_stars: list = []
    for y, line in enumerate(lines):
        all_stars.extend([(x, y) for x, n in enumerate(line.strip()) if n == "*"])
    ratio_sums: list = []
    for star in all_stars:
        gear_parts: list = []
        gear_index: list = []
        for y in range(star[1] - 1, star[1] + 2):
            for x in range(star[0] - 1, star[0] + 2):
                if (
                    x in parts
                    and y in parts[x]
                    and parts[x][y].get("range") not in gear_index
                ):
                    gear_parts.append(parts[x][y].get("part"))
                    gear_index.append(parts[x][y].get("range"))
        if len(gear_parts) == 2:
            ratio_sums.append(int(gear_parts[0]) * int(gear_parts[1]))
    return ratio_sums


def main():
    parts_sum, part_list = get_all_parts()
    print(sum(parts_sum))
    gears = get_gears(parts=part_list)
    print(sum(gears))


if __name__ == "__main__":
    main()
